debruijnSets = {2:'01', 3:'001011'}
debruijnConstants= {
            2:(2,2,0,1,0),
            3:(3,6,0,0,0),
            4:(4,14,0,1,3),
            6:(6,62,0,4,12),
            8:(8,254,0,8,56),
            12:(12,4094,0,34,868),
            16:(16,65534,0,130,15748),
            24:(24,16777214,0,254,4175880)
}
# I don't know actually know s, s' or t for v=2 or 3 debruin sets, but since I won't be doing the decode algorithm,
# because they're so short, I don't need to.

def interleaveSeqs(a, b):
    assert len(a) == len(b)
    # zip returns tuples. for x in t stuff flattens the tuples
    return ''.join(map(str, [x for t in zip(a, b) for x in t]))


def ConditionB(a, v, n):
    # This comes from section III.A, on page 4.
    # a is doubly punctured.
    ov = '0' * v
    ovm1 = '0' * (v - 1)
    lv = '1' * v
    lvm1 = '1' * (v - 1)
    assert ov not in a
    assert ovm1 in a
    assert lv not in a
    assert lvm1 in a
    # n is even, but not a multiple of 4.
    assert n % 2 == 0
    assert n % 4 != 0
    assert n == 2 ** v - 2
    return True

#these two functions just make the code a bit easier to read.
def Zeroes(v):
    return '0' * v


def Ones(v):
    return '1' * v


def deBruijnConstructionEven(a, v, n):
    assert ConditionB(a, v, n)
    # construct b
    # change a sequence of v-1 zeroes to v+1 zeroes
    t = a.replace(Zeroes(v - 1), Zeroes(v + 1), 1)
    # change a sequence of v-1 ones to v+1 ones.
    b = t.replace(Ones(v - 1), Ones(v + 1), 1)
    halfn = int(n / 2)
    dp = interleaveSeqs(b * halfn, a * (halfn + 2))
    # look, you're going to have to read [Mitchel et al, 1996] to make sense of d' and d constructions.
    print("t: %s" % str(dp.index(interleaveSeqs(Ones(v-1), Zeroes(v-1)))))
    d = dp.replace(interleaveSeqs(Ones(v - 1), Zeroes(v - 1)), interleaveSeqs(Ones(v), Zeroes(v)), 1)
    assert ConditionB(d, 2 * v, n * (n + 4) + 2)
    return d

#001011
def e(x):  # a decoder for a
    if len(x) == 3:
        return {'001': 0, '010': 1, '101': 2, '011': 3, '110': 4, '100': 5}[x]
    else:
        return deBruijnDecodeEven(x)


def moduloSystemSolver1(a,m1,b1,b2,m2):
    for i in range(0,m2):
        aa=(a+i*m1)%m2
        if (aa == b1)or(aa == b2):
            return aa

def moduloSystemSolver2(a,m1,b,m2):
    for i in range(0,m2):
        aa=(a+i*m1)%m2
        if  aa == b:
            return (a+i*m1)

def ep(ex,x): # a decoder for b.
    # I don't want to do a full set of recursions for E'(x) as well as E(x), so this function assumes the caller will
    # get and cache E(x), then call E'(x)
    s=debruijnSets[len(x)][3]
    sp=debruijnSets[len(x)][4]
    if x <= s:
        return ex
    elif x<= sp:
        return ex+2
    else:
        return ex+4

def deBruijnDecodeEven(x):
    v=len(x)
    n=debruijnSets[v][2]
    y=x[0:v:2]
    z=x[1:v:2]
    assert x == interleaveSeqs(y, z)
    ey=e(y)
    ez=e(y)
    epy=ep(ey,y)
    epz=ep(ez,z)
    fpx=0       #declaration is a placeholder so that I don't get lots of red underlines in PyCharm
    if y==Zeroes(int(v/2)):
        # m= E(z) mod n
        # m= s or s+1  mod n+4
        m=moduloSystemSolver1(ez,n,s,s+1,n+4)
        # F'(x)= 2m
        fpx=2*m
    elif y==Ones(int(v/2)):
        # m= E(z) mod n
        # m= sp+(2 or 3) mod n+4
        m=moduloSystemSolver1(ez,n,sp+2,sp+3,n+4)
        # F'(x)= 2m
        fpx=2*m
    elif z==Zeroes(int(v/2)):
        # m= E(y) mod n
        # m= s -(0 or 1) mod n+4
        m=moduloSystemSolver1(ey,n,s,s-1,n+4)
        # F'(x)= 2m+1
        fpx=2*m+1
    elif z==Ones(int(v/2)):
        # m= E(y) mod n
        # m= sp+(1 or 2) mod n+4
        m=moduloSystemSolver1(ey,n,s+1,s+2,n+4)
        # F'(x)= 2m+1
        fpx=2*m+1
    elif (ez-ey)%2 == 0:
        # m= E(z) mod n
        # m= E'(y) mod n+4
        m=moduloSystemSolver2(ez,n,epy,n+4)
        # F'(x)= 2m
        fpx=2*m
    elif (ez-ey)%2 == 1:
        # m= E(y) mod n
        # m= E'(z)-1 mod n+4
        m=moduloSystemSolver2(ey,n,epz,n+4)
        # F'(x)= 2m+1
        fpx = 2 * m+1
    t=debruijnSets[len(x)][4]
    if fpx < t:
        return fpx
    elif fpx>= t:
        return fpx+2
    elif x==interleaveSeqs(Ones(v),Zeroes(v)):
        return t
    elif x==interleaveSeqs(Ones(v),Zeroes(v)):
        return t+1

#25
for i in range(2, 25):
    if i in debruijnSets:
        print("%s: %s, %s" % (str(i), str(debruijnSets[i][1]), str(debruijnSets[i][2])))
    else:
        if (int(i / 2) in debruijnSets.keys()) and (i % 2 == 0):
            ss=debruijnSets[int(i / 2)]
            a = deBruijnConstructionEven(ss[0],ss[1],ss[2])
            v = debruijnSets[int(i / 2)][1] * 2
            n = len(a)
            s = debruijnSets[int(i / 2)][0].index(Zeroes(int(v/2) - 1))
            sp = debruijnSets[int(i / 2)][0].index(Ones(int(v/2) - 1))
            t= a.index(interleaveSeqs(Ones(int(v/2)), Zeroes(int(v/2))))
            print("t: %s"%int(t))
            ss=debruijnSets[i] = (a, v, n, s, sp, t)
            print("v={v:d} n={n:d} s={s:d} s'={sp:d} t={t:d}".format(v=ss[1],n=ss[2],s=ss[3],sp=ss[4],t=ss[5]))

# with open("Debruijn Sequences", "w") as f:
#     for i in debruijnSets.keys():
#         print("%s, %s" % (str(debruijnSets[i][1]), str(debruijnSets[i][2])), file=f)
#     print("", file=f)
#     for i in debruijnSets.keys():
#         print("%s:\n %s\n" % (str(debruijnSets[i][1]), str(debruijnSets[i][0])), file=f)
#
# d=deBruijnConstructionEven('001011',3,6)
# print(d)
# print(len(d))
# aa='00000100110110101011100101000011001111101001000101100011101111'
# assert d==aa
