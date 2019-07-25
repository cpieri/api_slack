import requests
from error import *
from get_all_users_slack import *
from invite_users import *

def create_channel(token):
	print ('Your token is: {token}'.format(token=token))
	is_private = input('Do you want a private channel ? [yes/no]\t')
	channel_name = input('What do you want to call your channel ?\t')
	if is_private == 'Y' or is_private == 'Yes' or is_private == 'y' or is_private == 'yes':
		url = 'https://slack.com/api/groups.create?token={token}&name={name}'.format(token=token, name=channel_name)
		channel = 'group'
	elif is_private == 'N' or is_private == 'No' or is_private == 'no' or is_private == 'n':
		url = 'https://slack.com/api/channels.create?token={token}&name={name}'.format(token=token, name=channel_name)
		channel = 'channel'
	else:
		error('Please you can choose if the channel is private or not')
	response = requests.post(url).json()
	if response['ok'] == False:
		error('Error: {error}'.format(error=response['error']))
	new_chan_id = response[channel]['id']
	invite = input('Do you want to invite everyone to this channel ? [yes/no]\t')
	if invite == 'Y' or invite == 'Yes' or invite == 'y' or invite == 'yes':
		users = get_all_users(token)
		invite_users2chan(users, new_chan_id, token, is_private)
	else:
		print ('Okay!! Good Bye')

