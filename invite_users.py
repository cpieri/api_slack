import requests
import time
from error import *

def invite_users2chan(users, chan_id, token, is_private):
	if is_private == 'Y' or is_private == 'Yes' or is_private == 'y' or is_private == 'yes':
		channel = 'groups'
	elif is_private == 'N' or is_private == 'No' or is_private == 'no' or is_private == 'n':
		channel = 'channels'
	for user in users:
		params = {
			'token': token,
			'channel': chan_id,
			'user': user['id']
		}
		r = requests.post('https://piscines101.slack.com/api/{private}.invite'.format(private=channel), params)
		print(user['name'], r['ok'])
		time.sleep(1)
