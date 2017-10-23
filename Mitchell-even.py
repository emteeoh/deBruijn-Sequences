
def interleaveSeqs(a,b):
    assert len(a)== len(b)
    # zip returns tuples. for x in t stuff flattens the tuples
    return ''.join(map(str,[x for t in zip (a,b) for x in t]))

def ConditionB(a,v,n):
    # This comes from section III.A, on page 4.
    # a is doubly punctured.
    ov='0'*v
    ovm1='0'*(v-1)
    lv='1'*v
    lvm1='1'*(v-1)
    assert ov not in a
    assert ovm1 in a
    assert lv not in a
    assert lvm1 in a
    # n is even, but not a multiple of 4.
    assert n%2==0
    assert n%4!=0
    assert n == 2**v-2
    return True

def Zeroes(v):
    return '0'*v
def Ones(v):
    return '1'*v

def deBruijnConstructionEven(a,v,n):
    assert ConditionB(a,v,n)
    # construct b
    # change a sequence of v-1 zeroes to v+1 zeroes
    t = a.replace(Zeroes(v-1),Zeroes(v+1),1)
    # change a sequence of v-1 ones to v+1 ones.
    b = t.replace(Ones(v-1),Ones(v+1),1)
    halfn=int(n/2)
    dp = interleaveSeqs(b*halfn,a*(halfn+2))
    # look, you're going to have to read [Mitchel et al, 1996] to make sense of d' and d constructions.
    d=dp.replace(interleaveSeqs(Ones(v-1),Zeroes(v-1)),interleaveSeqs(Ones(v),Zeroes(v)),1)
    assert ConditionB(d,2*v,n*(n+4)+2)
    return d

def e(x):  # a decoder for a
    if len(x)==3:
        return{'001':0,'010':1,'101':2,'011':3,'110':4,'100':5}[x]
    else:
        return deBruijnDecodeEven(x,len(x),2**len(x))


def deBruijnDecodeEven(x,v,n):
    pass



a='001011'; v=3; n=6
debruijnSets = {2:('01',2,2),3:('001011',3,6)}
for i in range(2,25):
    if i in debruijnSets:
        print("%s: %s, %s" % (str(i), str(debruijnSets[i][1]), str(debruijnSets[i][2])))
    else:
        if (int(i/2) in debruijnSets.keys()) and (i%2==0):
            a = deBruijnConstructionEven(*debruijnSets[int(i/2)])
            v= debruijnSets[int(i/2)][1]*2
            n= len(a)
            debruijnSets[i]=(a,v,n)
            print("%s: %s, %s" % (str(i), str(debruijnSets[i][1]), str(debruijnSets[i][2])))

with open("Debruijn Sequences","w") as f:
    for i in debruijnSets.keys():
        print("%s, %s" % (str(debruijnSets[i][1]), str(debruijnSets[i][2])),file=f)
    print("",file=f)
    for i in debruijnSets.keys():
        print("%s:\n %s\n" % (str(debruijnSets[i][1]), str(debruijnSets[i][0])),file=f)


# d=deBruijnConstructionEven('001011',3,6)
# print(d)
# print(len(d))
# aa='00000100110110101011100101000011001111101001000101100011101111'
# assert d==aa

