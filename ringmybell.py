from freesound.__init__ import *
Freesound.set_api_key('2623a9181cc64aa398f247971b1147e6')

import serial
import random
import urllib

def catchDoorbell(string_in):
    string_in = string_in.strip()
    if string_in == 'dingdong':
        print(string_in)
        fetchDoorbellRing()
    


def fetchDoorbellRing():
    print "Searching for doorbell:"
    print "----------------------------"
    results = Sound.search(q="doorbell",sort="rating_desc")
    print "Num results: " + str(results['num_results'])
    r = random.randint(0, results['num_results'])
    sound = random.sample(results['sounds'],1)[0]
    print "\t- " + sound['original_filename'] + " by " + sound['user']['username']
    print "\t-" + sound['preview-lq-mp3'] + "\n"
    # Sound.retrieve(Sound, sound['original_filename'])
    # f=file(sound['original_filename'], 'w')
    url=urllib.urlretrieve(sound['preview-lq-mp3'], "doorbell.mp3")
    print "download completed"
    


ser = serial.Serial('/dev/tty.usbmodemfa131', 9600)
while 1:
    catchDoorbell(ser.readline())




