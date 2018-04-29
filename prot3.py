#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import unirest #import unirest
import json #import json library
import re
from urllib2 import Request, urlopen, URLError #import libraries
from IPython.display import Audio


fs = 44100 # sampling frequency, Hz
fc = 440  # carrier frequency, Hz
fm = 220  # modulation frequency, Hz

T = 10 # seconds
twopi = 2*np.pi

t = np.linspace(0, T, int(T*fs), endpoint=False) # time variable

# Produce ramp from 0 to 1
beta = np.linspace(0, 1, int(T*fs))


output = np.sin(twopi*fc*t + beta*np.sin(twopi*fm*t))

Audio(output, rate=fs)
