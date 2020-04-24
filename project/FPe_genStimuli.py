
###############################################################################
# Task e: FPe_genStimuli.py (Section 4.5) (30%)
################
#
# Implement the body of this script:
#
#	Make 100 speech-noise pairs as stimuli for the experiment
#
#	You must NOT use/import	any other modules, apart from those in "lib" folder, "numpy", "os", "sys" and "random"
#
#	Refer to Section 4.5 in "../LING402_FP.pdf" for requirements
#
###############################################################################


import sys
import os
import random
import numpy as np
from lib.Waveform import Waveform
from lib.WAVWriter import WAVWriter
from lib.WAVReader import WAVReader
from lib.DSP_Tools import snr
### IMPORT MODULE(S) ABOVE THIS LINE ###

    
    
if not len(sys.argv) == 5:
    raise SystemExit("Usage: {} dir_wavs dir_stimuli file_wn etc/wn_idx.txt".format(sys.argv[0]))



### INSERT YOUR CODE BELOW THIS LINE ###

def setSNR(speech, noise, SNRtar):
    ratio = 10 ** (SNRtar / 10)
    ssum = 0
    nsum = 0
    
    for elem in speech:
        ssum += elem ** 2
        
    for elem in noise:
        nsum += elem ** 2
        
    k = np.sqrt(ssum / (ratio * nsum))[0]
    
    for i, element in enumerate(noise):
        noise[i] = (element*k)
    
    return (noise, k)

reading = sys.argv[1]
writing = sys.argv[2]
wnpath = sys.argv[3]
txtpath = sys.argv[4]

#reading = './wavs/'
#writing = './stimuli/'
#wnpath = './resources/wn.wav'
#txtpath = './etc/wn_idx.txt'

wn = WAVReader(wnpath)
wndata = wn.getData()
wnindex = len(wndata)
directory = os.fsencode(reading)
counter = 0
mylist = [None] * 100



for file in os.listdir(directory):
    filein = reading + file.decode('utf-8')
    wav = WAVReader(filein)
    wavdata = wav.getData()
#    print(type(wavdata.tolist()))
    wavindex = len(wavdata)
    maxstart = wnindex - wavindex
    randstart = random.randint(0, maxstart)
    filename = file.decode('utf-8')
    txtout = filename + '\t' + str(randstart) + '\n'
    mylist[counter] = txtout
    counter += 1
    
    adjusted = setSNR(wavdata, wndata[randstart : randstart + wavindex], 0)[0]
    twod = np.arange(wavindex*2).reshape(wavindex, 2)
    
    twodleft = []
    twodright = []
    
    for i in range(wavindex):
        s = wavdata[i][0]
        n = adjusted[i][0]
        twodleft.append(s)
        twodright.append(n)
        
    twod = np.array(list(zip(twodleft, twodright)))
    wavname = writing + filename
    wavtosave = WAVWriter(wavname, twod)
    wavtosave.write()


mylist.sort()
for elem in mylist:
    with open(txtpath, "a") as myfile:
        myfile.write(elem)

# To remove the last newline character
with open(txtpath, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

