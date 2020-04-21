import sys
from slack_token import token
from clean_channel import *
from create_channel import *
from invite_channel import *
from list_channel import *
from user_list_in_chan import *

def	choose():
	ask = """Welcome !! Here you can choose to perform actions easily on your slack :)\nChoose a number:
	1) for delete all messages from specific channel
	2) for create new channel or private channel
	3) for invite users to an existing channel
	4) for list all channel
	5) for list all user in channel
	6) for exit\n"""
	user_response = input(ask)
	return (int(user_response))

def exit():
	print ('Good Bye my Friend !!')
	sys.exit()

if __name__ == "__main__":
	response = choose()
	if response == 1:
		channel = input('Okay, Please enter the name of channel that you want clean:\t')
		clean_channel(channel, token)
	if response == 2:
		create_channel(token)
	if response == 3:
		invite_channel(token)
	if response == 4:
		list_channel(token)
	if response == 5:
		channel = input('Okay, Please enter the name of channel that you want clean:\t')
		list_user_in_chan(channel, token)
	if response == 6:
		exit()
