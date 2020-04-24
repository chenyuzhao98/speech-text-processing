# SampleSine.py -- Sampling of Sinusoids
# 
# genSineWave: retrieve samples from sine wave
# 
# Python (c) 2019 Yan Tang University of Illinois at Urbana-Champaign (UIUC)
#
# Created: March 13, 2019

import numpy as np
import math


class SampleSine:
    def __init__(self, freq=1000, amp_peak=1, phase=0):
        self.freq = freq            # sine frequency (Hz)
        self.amp_peak = amp_peak    # sine peak amplitude 
        self.phase = phase          # sine phase (degrees)

        # convert frquency to angular frequency
        self.rfreq = 2.0 * math.pi * self.freq     
        # convert phase in radians
        self.rphase = 2.0 * math.pi * self.phase / 360.0


    def genSineWave(self, time):
        # retuen sample sine function
        return self.amp_peak * np.sin(self.rfreq * time - self.rphase)



