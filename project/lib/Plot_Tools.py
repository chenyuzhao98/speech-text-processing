# Plot_Tools.py -- a set of functions for visualisation purposes
#
# newFigure: create a new figure handle
# showFigure: show a figure handle
# plotSignal: plot the wavform as the function of time
# plotHist: visualise the distribution of all the samples. 
#           The kernel density estimation curve for the distribution can be showed as an option
#
# Python (c) 2019 Yan Tang University of Illinois at Urbana-Champaign (UIUC)
#
# Created: March 14, 2019
# Modified: November 27, 2019


import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdfs


def plotSpectgram(spectgram, duration, fs, fid=1, title=""):
    gcf = newFigure(fid)

    plt.imshow(spectgram, cmap='gray_r', aspect="auto", extent=[0, duration, 0, round(fs/2)], vmin = 0, vmax = 3)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    return gcf

def plotSpect(signal, fid=1, title="", style="", legend=[], ylabel="Magnitude"):
    gcf = newFigure(fid)
    fmax = round(signal.sampleRate/2)
    x = np.arange(signal.nb_sample) * (fmax/signal.nb_sample)
    
    plt.plot(x, signal.data, style)
    # plt.ylim(0, 0)
    
    plt.xlim(0, x[len(x)-1])

    plt.xlabel('Frequency (Hz)')
    plt.ylabel(ylabel)
    plt.title(title)
    if legend:
        plt.legend(legend)

    # plt.show()
    return gcf

def plotSignal(signal, fid=1, title="", style="", legend=[], ylabel=""):
    gcf = newFigure(fid)
    x = np.arange(signal.nb_sample) / signal.sampleRate
    plt.plot(x, signal.data, style)
    # plt.ylim(0, 0)
    plt.xlim(0, x[len(x)-1])

    plt.xlabel('Time (s)')
    plt.ylabel(ylabel)
    plt.title(title)
    if legend:
        plt.legend(legend)

    # plt.show()
    return gcf


def plotHist(signal, doKDE=False, title=''):
    plt.figure(2)
    if doKDE:
        str_ylabel = 'Density'
        para_kde = {"color": "k", "lw": 0.9, "label": "KDE"}
    else:
        str_ylabel = 'Count'
        para_kde = {}

    sb.distplot(signal.data, bins=99, kde=doKDE, kde_kws=para_kde)
    plt.xlabel('Amplitude')
    plt.ylabel(str_ylabel)
    plt.title(title)
    # plt.show()


def newFigure(fid=1):
    fig = plt.figure(fid)
    return fig


def showFigure():
    plt.show()

def save2PDF(fname, figs):
    handle = pdfs(fname)
    try:
        for fig in figs:
            handle.savefig(fig)
    except:
        print("Errors have occurred while saving PDFs!")
    finally:
        handle.close()