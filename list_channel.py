import requests
from error import *

def list_channel(token):
	print ('Your token is: {token}'.format(token=token))
	pink = '\033[38;5;206m'
	cyan = '\033[36m'
	endl = '\033[0m'
	channels = requests.get('https://slack.com/api/{type}.list?limit=100&token={t}&types=public_channel,private_channel'.format(type='conversations', t=token)).json()
	chans = channels['channels']
	for chan in chans:
		if chan['is_private']:
			print (pink + 'Channel privé  : {name}'.format(name=chan['name']) + endl)
		else:
			print (cyan + 'Channel public : {name}'.format(name=chan['name']) + endl)