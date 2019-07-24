import requests
import time
import sys
from slack_token import token 

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ('Please enter a name of channel to clean !')
		sys.exit()
	print ('Your token is: {token}'.format(token=token))
	chan_to_find = sys.argv[1]
	response = requests.get('https://slack.com/api/channels.list?limit=100&token={token}'.format(token=token)).json()
	if response['ok'] == False:
		print ('Error: {error}'.format(error=response['error']))
		sys.exit()
	chan_id = False
	for channel in response['channels']:
		if channel['name'] == chan_to_find:
			chan_id = channel['id']
			print ('The channel "{chan}" have the id "{id}"'.format(chan=chan_to_find, id=chan_id))
	if chan_id == False:
		print ('Error: Your channel doesn\'t exist !')
		sys.exit()
	confirmation = input('Really want to delete all messages from this channel ? [y/n]')
	if confirmation == 'y':
		response = requests.get('https://slack.com/api/channels.history?count=1000&channel={id}&token={token}'.format(id=chan_id, token=token)).json()
		if response['ok'] == False:
			print ('Error: {error}'.format(error=response['error']))
			sys.exit()
		for msg in response['messages']:
			ts = msg['ts']
			res = requests.post('https://slack.com/api/chat.delete?ts={ts2del}&channel={chan_id}&token={token}'.format(ts2del=ts, chan_id=chan_id, token=token))
			print (res)
	else:
		print ('Okay, you\'re not sure.')
