"""
c-ary   base C
span v  refers to the size of tuples in the deBruijn sequence.
punctured   remove a 0 from 0**v in a span v sequence. pseudo-random-sequence
double-punctured  remove a 1 from 1**v
s=(s0,s1,s2,...,sn)
t=(t0,t1,t2,...,tn)
I(s,t)=(s0,t0,s1,t1,s2,t2,...,sn,tn)


Condition A:
  a is a c-ary v-window sequence of period n.
  n is even
  0**(v) is not an element of a
  0**(v-1) is at position 0 at least.
"""
def conditionA(a,n,v):
    res=False
    ov='0'*v
    ovm1='0'*(v-1)
    if (n%2)==0:
        res =  True
    try:
        a.index(ov)
    except ValueError:
        res=res&True
    if a[0:v-2] == ovm1:
        res=res&True
    return res

def interleaveSeqs(a,b):
    assert len(a)== len(b)
    return ''.join(map(str,[x for t in zip (a,b) for x in t]))   #zip returns tuples. for x in t stuff flattens the tuples.


def deBruijnConstruction():
    n=6
    c=2
    v=3
    a='001011'
    assert conditionA(a,n,v)
    b='00'+a
    return interleaveSeqs(b*int(n/2),a*int(1+n/2))
# d is a 2v window of n'=n(n+2)
# for ncv 632, v'=6 n'=48
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

def e(x):
    if len(x)==3:
        return{'000':0,'001':1,'010':2,'101':3,'011':4,'110':5,'100':6,'111':7}[x]
    else:
        deBruijnDecode(x)

def deBruijnDecode(x,d):
    y=x[0:len(x):2]
    z=x[1:len(x):2]
    ez=e(z)
    ey=e(y)
    c3=(y=='0'*(len(x)/2))
    c4=(z=='0'*(len(x)/2))
    c5=((ez-ey)%2==0)
    c6=((ez-ey)%2==1)
    assert (c5!=c6)
    c1= c3 or c5
    c2 = c4 or c6
    assert (c1 != c2)
# if c6 then m1=E(y), m2=E(z)+1 but if c3|c4?
# if c5 then m1=E(z), m2=E(y)+2 but if
d=deBruijnConstruction()
l=[]
for i in range(len(d)-6):
    l.append(d[i:i+6])
'''
for e in sorted(l):
    print(e)
print(d)
'''
deBruijnDecode('011100',d)
