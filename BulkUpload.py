#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os 
import time
import random
import requests
from os import listdir
from os.path import isfile, join 
from random import randint
from InstaAPI import InstagramAPI

request = urlopen('https://api.nasa.gov/planetary/apod?api_key=1HHTiK7TQC5QWyOMW2RTDnyuWSiDFYChaAues6PX')
PhotoLocation = request.url
IGUSER = "mordecai333"
PASSWD = "shitghost2"

CaptionList = ["Astronomy compels the soul to look upward, and leads us from this world to another.", "The contemplation of celestial things will make a man both speak and think more sublimely and magnificently when he descends to human affairs.", "The Universe, so far as we can observe it, is a wonderful and immense engine; its extent, its order, its beauty, its cruelty, makes it alike impressive.", "We need to have people up there who can communicate what it feels like, not just pilots and engineers. — Buzz Aldrin"]
IGCaption = random.choice(CaptionList)

os.chdir(PhotoLocation)
ShowMeWhatYouGot = [f for f in listdir(PhotoLocation)if isfile(join(PhotoLocation, f))]
print("SHOW ME WHAT YOU GOT, Pics in folder:"+ str(len(ShowMeWhatYouGot)))

igapi = InstagramAPI(LogInName, Password)
print("logging in...")
igapi.login()
print("done!")

for i in range(len(ShowMeWhatYouGot)):
	picture = ShowMeWhatYouGot[i]
	print ("Progress :" + str([i+1]) + " of " + str(len(ShowMeWhatYouGot)))

	# print("Checkin:" str([i+1])+ " of " + str (len(ShowMeWhatYouGot)))
	print("Putting this dank shit on the Ig:" + picture)
	igapi.uploadPhoto(picture, caption=IGCaption, upload_id=None)
	n = randint(600, 120)
	print("Sleeping for"+ str(n) + "seconds")
	time.sleep(n)