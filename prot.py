#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import unirest #import unirest
import os,sys,re,json
from urllib2 import Request, urlopen, URLError #import libraries
import math
from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio
import time as t

def silence(f):
    def silenced(f,g):
        silenced=''
    return silenced

class NoStdStreams(object):
    def __init__(self,stdout = None, stderr = None):
        self.devnull = open(os.devnull,'w')
        self._stdout = stdout or self.devnull or sys.stdout
        self._stderr = stderr or self.devnull or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        self.devnull.close()

def ps(lng, fq):
	#	See http://en.wikipedia.org/wiki/Bit_rate#Audio
	BITRATE = 16000 #number of frames per second/frameset.      
	
	#See http://www.phy.mtu.edu/~suits/notefreqs.html
	FREQUENCY = fq #Hz, waves per second, 261.63=C4-note.
	LENGTH = lng #seconds to play sound
	
	NUMBEROFFRAMES = int(BITRATE * LENGTH)
	RESTFRAMES = NUMBEROFFRAMES % BITRATE
	WAVEDATA = ''    
	
	for x in xrange(NUMBEROFFRAMES):
	   WAVEDATA += chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))    
	
	#fill remainder of frameset with silence
	for x in xrange(RESTFRAMES): 
	    WAVEDATA += chr(128)
	
	p = PyAudio()
	stream = p.open(
	    format=p.get_format_from_width(1),
	    channels=1,
	    rate=BITRATE,
	    output=True,
	    )
	stream.write(WAVEDATA)
	stream.stop_stream()
	stream.close()
	p.terminate()

def resp():
    response = unirest.get("https://api.particle.io/v1/devices/30002a001747343438323536/cm?access_token=aae9e607667b4dc3fed9ffa24402c68e0d22406c")
    raw      = response.raw_body
   # print(raw)
    return raw

def reg_ex(raw):
	cm = re.search('(?<=result":).*,"core',raw)
	return np.float64(cm.group()[:-6])


'''
#plt.axis([0, 10, 0, 1])
for i in range(10):
    raw = resp()
    y = reg_ex(raw)
    plt.scatter(i, round(y,2))
    plt.pause(0.05) 
    print(reg_ex(raw))
plt.show()
'''

init = t.time()
while True:
	dist = reg_ex(resp())
	if init-t.time() < 30:
		if (dist > -1) and (dist < 50):
			ps(0.2,8000)
			print('Close: {}'.format(dist))
		elif (dist > 50) and (dist < 100):
			ps(0.2,4000)
			print('Semi-close:{}'.format(dist))
		elif (dist > 100) and (dist < 150):
			ps(0.2,2000)
			print('Normal: {}'.format(dist))
		elif (dist > 150) and (dist < 200):
			ps(0.2,1000)
			print('Far: {}'.format(dist))
		else:
			print('Out of range: {}'.format(dist))
	t.sleep(0.3)


