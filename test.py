from scipy import fftpack, arange
import numpy
import math

def printArray(arr):
    s = ''
    for b in arr:
        s += str(b) + ' '
    print s

def printComplexArray(arr):
    s = ''
    for b in arr:
        val = abs(b)
        s += str(val if val > 0.1 else 0) + ' '
    print s

def printIfftArray(arr):
    s = ''
    for b in arr:
        s += str(b.real) + ' '
    print s


# Read data from device
# dataArr = [math.sin(x*2*3.14/16.0) for x in range(16)]
Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = arange(0,1,Ts) # time vector

ff = 5;   # frequency of the signal
dataArr = numpy.sin(2*math.pi*ff*t)

n = len(dataArr)
# Return the maximum of the absolute value of all samples in a fragment.
transformedData = fftpack.fft(dataArr)/n

transformedData = transformedData[range(n/2)]

printArray(dataArr)
print
printComplexArray(transformedData)
print
# printComplexArray(fftpack.ifft([0, 4, 0, 0, 0, 0, 0, 4]))
# printArray(fftpack.ifft([0, 8, 0, 0, 0, 0, 0, 0]))
# printArray(fftpack.ifft([8, 0, 0, 0, 0, 0, 0, 0]))