# Waveform.py -- a set of functions required for basic DSP
# 
# normaliseRMS: adjust root-mean-squre (RMS) of the signal to the target RMS.
# snr: compute speech-to-noise ratio of given speech and noise signals.
# rms: compute RMS of the signal
# 
# Python (c) 2019 Yan Tang University of Illinois at Urbana-Champaign (UIUC)
#
# Created: March 14, 2019
# Modified: November 11, 2019


import numpy as np
from lib.Waveform import Waveform

def normaliseRMS(x, tarRMS):
    # detech the number of channels in the signal
    # enable the function to deal with signals that contain more than one channel
    dim = np.shape(x) 
    nb_sample = np.max(dim) # number of samples
    nb_chan = np.min(dim)   # number of channels

    k = tarRMS * np.sqrt(nb_sample * nb_chan / (np.sum(x**2)))
    return k * x, k

def snr(s, n):
    return 10 * np.log10(np.sum(s**2) / np.sum(n**2))


def rms(x):
    # detech the number of channels in the signal
    # enable the function to deal with signals that contain more than one channel
    dim = np.shape(x) 
    nb_sample = np.max(dim) # number of samples
    nb_chan = np.min(dim)   # number of channels

    return np.sqrt(np.sum(x**2)/(nb_sample * nb_chan))

def scalesig(x, scalar=1.1):
    return x / (scalar * np.max(np.abs(x)))

# Make packing format for number-to-byte conversion and vise versa
def mkDataStructFMT(bits, total_samples):
    if bits == 8: 
        fmt = "%ib" % total_samples # 1-byte signed char
    elif bits == 16:
        fmt = "%ih" % total_samples # 2-byte shorts
    else:
        raise ValueError("Only supports 8- and 16-bit audio formats.")

    return fmt


# Implementation of Convolution of two waveforms
# take the input waveform x and impluse response h
def convolve(waveform_x, waveform_h):
    len_x = waveform_x.count()
    len_h = waveform_h.count()

    data_x = waveform_x.data
    data_h = waveform_h.data
    if len_x != len_h: # match the lengh of the two vectors
        dif = np.abs(len_x - len_h)

        padding = np.zeros((dif, 1), dtype = np.float)
        if len_x > len_h:
            data_h = np.concatenate((data_h, padding), axis=0)
        else:
            data_x = np.concatenate((data_x, padding), axis=0)

    # initialise an empty waveform for convoluation  
    y = Waveform(data_x.size, waveform_x.sampleRate)
    
    # for each output sample in y
    for idx_y in range(0, y.count()):  
        for idx_h in range(0, len_h):
            y.data[idx_y] += data_x[idx_y - idx_h] * data_h[idx_h]

    # return the convolved sequence
    return y

