debruijnSets = {2: '01', 3: '001011'}
debruijnConstants = {
    2: (2, 2, 0, 1, 0),
    3: (3, 6, 0, 2, 2),
    4: (4, 14, 0, 1, 3),
    6: (6, 62, 0, 4, 12),
    8: (8, 254, 0, 8, 56),
    12: (12, 4094, 0, 34, 868),
    16: (16, 65534, 0, 130, 15748),
    24: (24, 16777214, 0, 254, 4175880)
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


# these two functions just make the code a bit easier to read.
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
    d = dp.replace(interleaveSeqs(Ones(v - 1), Zeroes(v - 1)), interleaveSeqs(Ones(v), Zeroes(v)), 1)
    assert ConditionB(d, 2 * v, n * (n + 4) + 2)
    return d


# 001011
def e(x):  # a decoder for a
    if len(x) == 3:
        return {'001': 0, '010': 1, '101': 2, '011': 3, '110': 4, '100': 5}[x]
    elif len(x) == 2:
        return {'01': 0, '10': 1}[x]
    elif len(x) == 4:
        # 00010100111011
        return {'0001': 0, '0010': 1, '0101': 2, '1010': 3, '0100': 4, '1001': 5, '0011': 6, '0111': 7,
                '1110': 8, '1101': 9, '1011': 10, '0110': 11, '1100': 12, '1000': 3}
    else:
        return deBruijnDecodeEven(x)


# noinspection PyUnusedLocal
def moduloSystemSolver1(x, params):
    # a,m1,b1,b2,m2
    a = e(params[0])
    m1 = params[1]
    b1 = params[2]
    b2 = params[3]
    m2 = params[4]
    for i in range(0, m2):
        aa = (a + i * m1) % m2
        if (aa == b1) or (aa == b2):
            return aa

def ep(x,v):
    s=debruijnConstants[v][2]
    sp=debruijnConstants[v][3]
    if 0<=x<=s:
        print("0<=x<=s")
        offset=0
    elif s<x<=sp:
        print("s<x<=s'")
        offset=2
    else:
        print("x>s'")
        offset=4
    print("E' offset is {}".format(offset))
    return(x+offset)

def moduloSystemSolver2(x, params):
    print(params)
    # a,m1,b,m2
    # this function solves the systems of equations:
    # /m= E(a) mod m1
    # \m= E'(b) mod m2
    #except that a and b are already E(y) and E(z). This function doesn't care which way 'round it is.
    # E' is calculated with t and using x.
    m1 = params[1]
    m2 = params[3]
    a = params[0]%m1
    b = params[2]%m2
    print("target: {}".format(b))
    print ("mods: {} {}".format(m1,m2))
    for i in range(0, m2):
        aa = (a + i * m1) % m2
        print(aa)
        if aa == b:
            r=i
            break
    return (a + r * m1)%m2

def deBruijnDecodeEven(x):
    v = len(x)
    print("v {}".format(v))
    if v == 3:
        result= {'001': 0, '010': 1, '101': 2, '011': 3, '110': 4, '100': 5}[x]
    elif v == 2:
        result = {'01': 0, '10': 1}[x]
    elif v == 4:
        result = {'0001': 0, '0010': 1, '0101': 2, '1010': 3, '0100': 4, '1001': 5, '0011': 6, '0111': 7,
                '1110': 8, '1101': 9, '1011': 10, '0110': 11, '1100': 12, '1000': 13}[x]
    else:
        n = debruijnConstants[v][1]
        t = debruijnConstants[len(x)][4]
        s = debruijnConstants[len(x)][2]
        sp = debruijnConstants[len(x)][3]
        y = x[0:v:2]
        z = x[1:v:2]
        print(y)
        print(z)
        if y == Zeroes(int(v / 2)):
            print ("Y zeroes")
            msolver = moduloSystemSolver1
            mparams = (z, n, s, s + 1, n + 4)
            fpparm = 0
        elif y == Ones(int(v / 2)):
            print ("Y Ones")
            msolver = moduloSystemSolver1
            mparams = (z, n, sp + 2, sp + 3, n + 4)
            fpparm = 0
        elif z == Zeroes(int(v / 2)):
            print ("z zeroes")
            msolver = moduloSystemSolver1
            mparams = (y, n, s, s - 1, n + 4)
            fpparm = 1
        elif z == Ones(int(v / 2)):
            print ("z Ones")
            msolver = moduloSystemSolver1
            mparams = (y, n, s + 1, s + 2, n + 4)
            fpparm = 1
        else:
            print("No zeroes.")
            ey = e(y)
            ez = e(z)
            fpparm = (e(z) - e(y)) % 2
            msolver = moduloSystemSolver2
            if fpparm == 0:
                print("E(z)-E(y) is even")
                mparams = (ez, n,ep(ey), n+4)
            else:
                print("E(z)-E(y) is odd")
                mparams = (ey, n,(ep(ez,int(v/2))-1)%n+4, n+4)
        # calc m
        m = msolver(x, mparams)
        print("m: {}".format(m))
        # calc f
        fpx = 2 * m + fpparm
        print ("fpx: {}".format(fpx))
        if x == interleaveSeqs(Ones(int(v / 2)), Zeroes(int(v / 2))):
            print("10*")
            offset = t
        elif x == interleaveSeqs(Zeroes(int(v / 2)), Ones(int(v / 2))):
            print("01*")
            offset = t + 1
        elif fpx < t:
            print("less than t, {}".format(t))
            offset = 0
        else:
            print("bigger than t {}".format(t))
            offset = 2
            print (fpx)
            print(offset)
        result =fpx+offset
        print(result)
    return result


# # 25
# for i in range(3, 25):
#     if i in debruijnSets:
#         # print("%s: %s, %s" % (str(i), str(debruijnConstants[i][0]), str(debruijnConstants[i][1])))
#         pass
#     else:
#         if (int(i / 2) in debruijnConstants.keys()) and (i % 2 == 0):
#             ss = int(i / 2)
#             a = deBruijnConstructionEven(debruijnSets[ss], debruijnConstants[ss][0], debruijnConstants[ss][1])
#             v = debruijnConstants[ss][0] * 2
#             n = len(a)
#             try:
#                 s = debruijnSets[ss].index(Zeroes(int(v / 2) - 1))
#                 sp = debruijnSets[ss].index(Ones(int(v / 2) - 1))
#                 t = a.index(interleaveSeqs(Ones(int(v / 2)), Zeroes(int(v / 2))))
#             except ValueError:
#                 print(debruijnConstants[int(i / 2)])
#                 print(debruijnSets[int(i / 2)])
#                 print(i)
#                 print(v)
#                 raise
#             ss = debruijnConstants[i] = (v, n, s, sp, t)
#             debruijnSets[i] = a
#             # print("v={v:d} n={n:d} s={s:d} s'={sp:d} t={t:d}".format(v=ss[0],n=ss[1],s=ss[2],sp=ss[3],t=ss[4]))

debruijnSets[6]=deBruijnConstructionEven('001011',3,6)
# ll = 6
# for i in range(0, len(debruijnSets[ll])):
#     target = (debruijnSets[ll] * 2)[i:i + ll]
#     pos=deBruijnDecodeEven(target)
#     if pos != i:
#         print(" {} didn't work. {} {}".format(target,i,pos))

print(deBruijnDecodeEven(debruijnSets[6][3:9]))

# x = 001001
# position is 3
# y=010
# z=001
# E(y)=1
# E(z)=0
# ez-ey=-1
# mss2(ey,n,ez,n+4) => mss2(1,62,0,66)
# s=0
# sp=4
# t=12
# F'(x)>s', so F(x)=F'(x)+4



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

# a=001011
# b=0000101111 mmmmnmnnnn
# x=001001
# Y=010 e(y)=1
# z=001 e(z)=0
# e'(z)= 2
# d'= 0m0m1m0m1n1m0n0n1n0n1m1m0m0m1n0m1n1n0n0n1m0m1m1m0n0m1n0n1n1n