

import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio

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

ps(0.2,5000)
