import sys
from slack_token import token
from clean_channel import *
from create_channel import *

def	choose():
	ask = """Welcome !! Here you can choose to perform actions easily on your slack :)\nChoose a number:
	1) for delete all messages from specific channel
	2) for create new channel or private channel
	3) for exit\n"""
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
		exit()
