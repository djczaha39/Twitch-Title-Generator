#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Twitch Stream Title Generator
# Writen by Jan Rokita
# https://rokita.me
#

import requests, random

token = "YOUR_ACCESS_TOKEN"
channel_name = "YOUR_TWITCH_USERNAME"

list1 = ["Watery", "Frozen", "Burning", "Firery", "Floating", "Dark", "Shadowed"]
list2 = ["Tower", "Dungeon", "Stronghold", "Fort", "Cave", "Gauntlet", "Palace", "Castle"]
list3 = ["Doom", "Dragons", "Dispair", "Moans", "Endless Puzzles", "Traps", "Wizards", "Darkness"]

def send_Request(token,title):
	headers = {
	    'Accept': 'application/vnd.twitchtv.v2+json',
	    'Authorization': 'OAuth '+token,
	}

	data = {
		'channel[status]': title,
	}

	requests.put('https://api.twitch.tv/kraken/channels/'+channel_name, headers=headers, params=data)

def gen_Title():
	sel1 = random.randint(0,len(list1)-1)
	sel2 = random.randint(0,len(list2)-1)
	sel3 = random.randint(0,len(list3)-1)

	return "The " + list1[sel1] + " " + list2[sel2] + " " + "of " + list3[sel3]

def main():
	title = gen_Title()
	send_Request(token, title+" ·٠•● "+channel_name+" ●•٠· ")
	print title+" ·٠•● "+channel_name+" ●•٠· "

main()
