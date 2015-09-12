import CosmicWaveModem.cosmicmodem as modem
import alsaaudio

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NORMAL)
inp.setchannels(1)
inp.setrate(4000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

dataStream = []

while True:
    # Read data from device
    l, data = inp.read() # length is 160 bytes
    decoded = modem.decode(bytearray(data))
    print decoded
    # dataStream.append(decoded)
