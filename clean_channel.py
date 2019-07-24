import requests
from error import *

def clean_channel(channel2clean, token):
	print ('Your token is: {token}'.format(token=token))
	chan_to_find = channel2clean
	response = requests.get('https://slack.com/api/channels.list?limit=100&token={token}'.format(token=token)).json()
	if response['ok'] == False:
		error('Error: {error}'.format(error=response['error']))
	chan_id = False
	for channel in response['channels']:
		if channel['name'] == chan_to_find:
			chan_id = channel['id']
			print ('The channel "{chan}" have the id "{id}"'.format(chan=chan_to_find, id=chan_id))
	if chan_id == False:
		error('Error: Your channel doesn\'t exist !')
	confirmation = input('Really want to delete all messages from this channel ? [y/n]')
	if confirmation == 'y':
		response = requests.get('https://slack.com/api/channels.history?count=1000&channel={id}&token={token}'.format(id=chan_id, token=token)).json()
		if response['ok'] == False:
			error('Error: {error}'.format(error=response['error']))
		for msg in response['messages']:
			ts = msg['ts']
			res = requests.post('https://slack.com/api/chat.delete?ts={ts2del}&channel={chan_id}&token={token}'.format(ts2del=ts, chan_id=chan_id, token=token))
			print (res)
	else:
		error('Okay, you\'re not sure.')
