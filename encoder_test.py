import CosmicWaveModem.cosmicmodem as modem

data = modem.encode("yo here's some test data")
open('data.wav', 'wb').write(data.getvalue())

'''
for char in "string":
    c = ord(char)
    print 'c', c
    for i in range(2):
        print (c >> 4*i) & 15
'''

print [f for f in modem.getFreqs("string")]