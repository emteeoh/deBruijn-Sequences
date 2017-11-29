from MitchellDecode import deBruijnEvenDecode, MitchellDecode
from generate import iterbruijn, iterdpdB

D16=[ i for i in iterbruijn(16)]+[0]*15
for i in range(len(D16)-16):
    j = deBruijnEvenDecode(D16[i:i+16])
    if i!=j:
        print (D16[i:i+16], i,j)
D16p = [ i for i in iterdpdB(16)]+[0]*15
for i in range(len(D16p)-16):
    j = MitchellDecode(D16p[i:i+16])
    if i!=j:
        print (D16[i:i+16], i,j)
