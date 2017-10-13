#!/usr/bin/env python

import time
import argparse
import random

import requests


def check_url(url):
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

	response = requests.get(url, headers = headers)
	if response.status_code != 200:
		print("{}\t{}\t{}".format(response.status_code, url, response.content))
		return
	else:
		print("{}\t{}".format(response.status_code, url, response.content))



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--file',
		dest='urls_list',
		required=True,
		help='file with urls')
	
	args = parser.parse_args()

	with open(args.urls_list, 'r') as f:
		for url in f.readlines():
				check_url(url)
				time.sleep(random.randint(1, 3))

