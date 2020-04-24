
###############################################################################
# Task d: FPd_genWhiteNoise.py (Section 4.4) (20%)
################
#
# Implement the body of this script:
#
#	Generate a 1-minute long white noise using a sampling frequency of 16000 Hz with an amplitude of 0.5, and save it as a WAV file. 
#
#	You must use the WhiteNoise class in FPc_WhiteNoise.py to generate the signal.
#
#	Define a method validateInput() to validate the value of the positional parameters for sampling frequency and duration in seconds. Both the values must be positive numbers. If any of the two inputs is invalid, the method should print out error messages and terminates the execution.
#
#	You must NOT use/import	any other modules, apart from those in "lib" folder, "numpy" and "sys"
#
#	Refer to Section 4.4 in "../LING402_FP.pdf" for other requirements
#
###############################################################################


import sys
from lib.Waveform import Waveform
from lib.WAVWriter import WAVWriter
from lib.WAVReader import WAVReader

from FPc_WhiteNoise import WhiteNoise
import lib.Plot_Tools as plot
from numpy.fft import fft
import numpy as np


### IMPORT MODULE(S) ABOVE THIS LINE ###

          

if not len(sys.argv) == 5:
    raise SystemExit("Usage: {} duration_s fs_Hz file_wn file_spect".format(sys.argv[0]))



### INSERT YOUR CODE BELOW THIS LINE ###

def validateInput(val1, val2):
    if val1 < 0 or val2 < 0:
        raise SystemExit("Please provide positive sampling frequency and duration values")


duration = int(sys.argv[1])
fs = int(sys.argv[2])
wavpath = sys.argv[3]
pdfpath = sys.argv[4]


#duration = 60
#fs = 16000
#wavpath = './noise/wn.wav'
#pdfpath = './etc/spect_wn.pdf'


validateInput(duration, fs)

nb_sample = int(fs * duration)

wavwn = Waveform(nb_sample, fs)
for t in range(0, nb_sample):
    wn = WhiteNoise(0.5)
    wavwn.data[t] = wn.genWhiteNoise()

wavfile = WAVWriter(wavpath, wavwn.data, fs, 16)
wavfile.write()



short_duration = 1
short_nb_sample = int(short_duration * fs)
short_wav = WAVReader(wavpath)


#print(len(short_wav.getData()))
fft_bins = fft(short_wav.getData()[:short_nb_sample], axis=0)
nb_bin = int(len(fft_bins)/2)
spect = Waveform(nb_bin, fs)
for t in range(nb_bin-1):
    spect.data[t] = 20 * np.log10(abs(fft_bins[t]))
graph = plot.plotSpect(spect, fid=1)
plot.save2PDF(pdfpath, [graph])
#plot.showFigure()
