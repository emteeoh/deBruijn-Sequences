
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

def deBruijnDecodeEven(a,v,n):
    pass

d=deBruijnConstructionEven('001011',3,6)
print(d)
aa='00000100110110101011100101000011001111101001000101100011101111'
assert d==aa
