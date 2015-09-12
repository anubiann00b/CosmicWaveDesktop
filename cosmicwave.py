import CosmicWaveModem.cosmicmodem as cosmicmodem
import alsaaudio

from scipy.signal import fftconvolve
from numpy import argmax, diff
from matplotlib.mlab import find

def parabolic(f, x):
    xv = 1/2. * (f[x-1] - f[x+1]) / (f[x-1] - 2 * f[x] + f[x+1]) + x
    yv = f[x] - 1/4. * (f[x-1] - f[x+1]) * (xv - x)
    return (xv, yv)

def freq_from_autocorr(sig, fs):
    # Calculate autocorrelation (same thing as convolution, but with 
    # one input reversed in time), and throw away the negative lags
    corr = fftconvolve(sig, sig[::-1], mode='full')
    corr = corr[len(corr)/2:]
    
    # Find the first low point
    d = diff(corr)
    start = find(d > 0)[0]
    
    # Find the next peak after the low point (other than 0 lag).  This bit is 
    # not reliable for long signals, due to the desired peak occurring between 
    # samples, and other peaks appearing higher.
    # Should use a weighting function to de-emphasize the peaks at longer lags.
    peak = argmax(corr[start:]) + start
    px, py = parabolic(corr, peak)
    
    return fs / px

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NORMAL)
inp.setchannels(1)
inp.setrate(4000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

dataStream = []

while True:
    # Read data from device
    l, data = inp.read() # length is 160 bytes
    freq = freq_from_autocorr(bytearray(data), 4000)*2
    dataStream.append(freq)
