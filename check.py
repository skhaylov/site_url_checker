#!/usr/bin/env python

import time
import argparse
import random

import requests


def check_url(url, user_agents):
	user_agent = user_agents[random.randint(0, len(user_agents) - 1)]
	headers = {'user-agent': user_agent}

	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		print("{}\t{}\t{}".format(response.status_code, url, response.content))
	else:
		print("{}\t{}".format(response.status_code, url, response.content))


def get_user_agents():
	with open('user_agents.txt', 'r') as f:
		return f.readlines()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--file',
		dest='urls_list',
		required=True,
		help='file with urls')
	
	args = parser.parse_args()

	with open(args.urls_list, 'r') as f:
		user_agents = get_user_agents()
		for url in f.readlines():
				check_url(url, user_agents)
				time.sleep(random.randint(2, 5))


