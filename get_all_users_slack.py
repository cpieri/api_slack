import requests
from error import *

def get_all_users(token):
	page = requests.get('https://slack.com/api/users.list?limit=100&token={}'.format(token)).json()
	users = page['members']
	while page['response_metadata']['next_cursor']:
		page = requests.get('https://slack.com/api/users.list?limit=100&cursor={}&token={}'.format(page['response_metadata']['next_cursor'], token)).json()
		users += page['members']
	return (users)
