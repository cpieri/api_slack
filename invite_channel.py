import requests
from error import *
from get_all_users_slack import *
from invite_users import *
from search_chan import *

def invite_channel(token):
	print ('Your token is: {token}'.format(token=token))
	is_private = input('Do you want a private channel ? [yes/no]\t')
	channel_name = input('What do you want to call your channel ?\t')
	chan_id = search_chan(channel_name, is_private, token)
	invite = input('Do you want to invite everyone to this channel ? [yes/no]\t')
	if invite == 'Y' or invite == 'Yes' or invite == 'y' or invite == 'yes':
		users = get_all_users(token)
		invite_users2chan(users, chan_id, token, is_private)
	else:
		print ('okay !')
