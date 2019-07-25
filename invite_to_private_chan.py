import requests
import time

token='xoxs-179666044467-234574484800-406440782452-bb3efc39d5'

logins_list =

print(len(logins_list))

chan_name = 'the_skunks'

channels = requests.get('https://slack.com/api/groups.list?limit=100&token={}'.format(token)).json()
print(channels)

for chan in channels['groups']:
    if chan['name'] == chan_name:
        chan_id = chan['id']
        print(chan_id)


page = requests.get('https://slack.com/api/users.list?limit=100&token={}'.format(token)).json()
slack_piscine_users = page['members']
while page['response_metadata']['next_cursor']:
    page = requests.get('https://slack.com/api/users.list?limit=100&cursor={}&token={}'.format(page['response_metadata']['next_cursor'], token)).json()
    slack_piscine_users += page['members']

for user in slack_piscine_users:
    if user['name'].lower() in logins_list:
        params = {
            'token': token,
            'channel': chan_id,
            'user': user['id']
        }
        r = requests.post('https://piscines101.slack.com/api/groups.invite', params)
        print(user['name'], r.text)
        time.sleep(1)
