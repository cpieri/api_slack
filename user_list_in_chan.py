import requests
from error import *

def list_user_in_chan(channel2clean, token):
	print ('Your token is: {token}'.format(token=token))
	chan_to_find = channel2clean
	response = requests.get('https://slack.com/api/conversations.list?limit=100&token={token}&types=public_channel,private_channel'.format(token=token)).json()
	if response['ok'] == False:
		error('Error: {error}'.format(error=response['error']))
	chan_id = False
	for channel in response['channels']:
		if channel['name'] == chan_to_find:
			chan_id = channel['id']
			print ('The channel "{chan}" have the id "{id}"'.format(chan=chan_to_find, id=chan_id))
	if chan_id == False:
		error('Error: Your channel doesn\'t exist !')
	confirmation = input('Really want to print all users from this channel ? [y/n]\t')
	if confirmation == 'y':
		response = requests.get('https://slack.com/api/conversations.members?channel={id}&token={token}'.format(id=chan_id, token=token)).json()
		if response['ok'] == False:
			error('Error: {error}'.format(error=response['error']))
		for member in response['members']:
			res = requests.post('https://slack.com/api/users.info?user={member}&token={token}'.format(member=member, token=token)).json()
			if res['ok'] == False:
				error('Error: {error}'.format(error=res['error']))
			else:
				user = res['user']
				print(user['name'])
	else:
		error('Okay, you\'re not sure.')
