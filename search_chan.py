import requests
from error import *

def search_chan(name, is_private, token):
	if is_private == 'Y' or is_private == 'Yes' or is_private == 'y' or is_private == 'yes':
		channel = 'groups'
	elif is_private == 'N' or is_private == 'No' or is_private == 'no' or is_private == 'n':
		channel = 'channels'
	channels = requests.get('https://slack.com/api/{type}.list?limit=100&token={t}'.format(type=channel, t=token)).json()
	for chan in channels[channel]:
		if chan['name'] == name:
			chan_id = chan['id']
			return (chan_id)
	return False
