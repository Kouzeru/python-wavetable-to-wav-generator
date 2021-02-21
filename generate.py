# wavetable to wav generator, written by Kouzeru - 2/14/2021
from math import ceil
period  = 8
smpRate = 440*16*period
duration= 8
filesize= smpRate*duration
waves=[
['p00.wav','0000000FF0000000'],
['p01.wav','000000FFFF000000'],
['p02.wav','0000FFFFFFFF0000'],
['p03.wav','00FFFFFFFFFFFF00'],
['p10.wav','0000000FF0000000'],
['p11.wav','000000FFFF000000'],
['p12.wav','0000FFFFFFFF0000'],
['p13.wav','00FFFFFFFFFFFF00'],
['p20.wav','0000000FF0000000'],
['p21.wav','000000FFFF000000'],
['p22.wav','0000FFFFFFFF0000'],
['p23.wav','00FFFFFFFFFFFF00'],
['p30.wav','0000000FF0000000'],
['p31.wav','000000FFFF000000'],
['p32.wav','0000FFFFFFFF0000'],
['p33.wav','00FFFFFFFFFFFF00'],
['v00.wav','0FFFFFFFFFFFFFFF'],
['v01.wav','0FFFFFFFFFFFFFF0'],
['v02.wav','0FFFFFFFFFFFFF00'],
['v03.wav','0FFFFFFFFFFFF000'],
['v04.wav','0FFFFFFFFFFF0000'],
['v05.wav','0FFFFFFFFFF00000'],
['v06.wav','0FFFFFFFFF000000'],
['v07.wav','0FFFFFFFF0000000'],
['v10.wav','0FFFFFFFFFFFFFFF'],
['v11.wav','0FFFFFFFFFFFFFF0'],
['v12.wav','0FFFFFFFFFFFFF00'],
['v13.wav','0FFFFFFFFFFFF000'],
['v14.wav','0FFFFFFFFFFF0000'],
['v15.wav','0FFFFFFFFFF00000'],
['v16.wav','0FFFFFFFFF000000'],
['v17.wav','0FFFFFFFF0000000'],
['saw.wav','0123456789ABCDEF'],
['tri.wav','0123456789ABCDEFFEDCBA9876543210'],
]

a,b=1,""
while True:
 a=(a>>1)|(((a&1)^((a>>1)&1))<<14)
 b+="F" if a&0x4000 else "0"
 if a==1:
   break
waves.append(['no0.wav',b])

a,b=23,""
while True:
 a=(a>>1)|(((a&1)^((a>>6)&1))<<14)
 b+="F" if a&0x4000 else "0"
 if a==23:
   break
waves.append(['no1.wav',b])

for k in waves:
    out = open(k[0],"wb")
    out.write(bytes('RIFF'.encode()))
    out.write(filesize.to_bytes(4,'little'))
    out.write(bytes('WAVEfmt '.encode()))
    out.write(bytes.fromhex("1000000001000100"))
    out.write(smpRate.to_bytes(4,'little'))
    out.write(smpRate.to_bytes(4,'little'))
    out.write(bytes.fromhex("0100080064617461"))
    b=[]
    for c in k[1]:
     a=127+int(c,16)*8
     for i in range(0,period):
      b.append(a)
    for i in range(0,ceil(filesize/len(b))):
     out.write(bytes(b))
    out.close()