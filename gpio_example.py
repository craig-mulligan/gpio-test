#!/usr/bin/python
# import RPi.GPIO as GPIO
# import time

# a = GPIO.VERSION
# print a

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# print "gpioexample"

# while True:
#     input_state = GPIO.input(17)
#     if input_state == False:
#         print('Button Pressed')
#         time.sleep(0.2)

import json, time, random, math, urllib, urllib2, pycurl, subprocess, sys

# returns the appropriate google speech url for a particular phrase
def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
    parameters = {'q': phrase}
    data = urllib.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL

# function to download an mp3 file for a particular phrase, used for testing
def downloadSpeechFromText(phrase, fileName):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    print googleSpeechURL
    downloadFile(googleSpeechURL, fileName)

# function to download a file from a url, used for testing
def downloadFile(url, fileName):
    fp = open(fileName, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

# output phrase to audio using mplayer
def speakSpeechFromText(phrase):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    subprocess.call(["mplayer",googleSpeechURL], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#download a speech file from google
#downloadSpeechFromText("hello, how are you today", "./downloadedFile.mp3")
#output phrase to audio
speakSpeechFromText("hello, how are you today")