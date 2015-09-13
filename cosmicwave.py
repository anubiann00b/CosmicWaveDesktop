import CosmicWaveModem.cosmicmodem as modem
import alsaaudio
from time import time
from time import sleep

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL)
inp.setchannels(1)
inp.setrate(modem.BITRATE) # 8000
inp.setformat(alsaaudio.PCM_FORMAT_U8)
inp.setperiodsize(modem.FRAMES) # 4000

dataStream = []

charList = []

def onData(val):
    print "YO THIS SHIT IS GETTING CALLED: ", val
    global charList
    charList.append(chr(val))

modem.registerOnDecodedDataListener(onData)

while True:
    startTime = time()
    l, data = inp.read()
    decoded = modem.decode(bytearray(data))
    # print 'time: ' + str(time() - startTime)
    print charList
    # print decoded
    # dataStream.append(decoded)
