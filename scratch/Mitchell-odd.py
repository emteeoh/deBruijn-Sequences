def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def conditionA(a, n, v):
    res = False
    ov = '0' * v
    ovm1 = '0' * (v - 1)
    if (n % 2) == 0:
        res = True
    try:
        a.index(ov)
    except ValueError:
        res = res and True
    if a[0:v - 2] == ovm1:
        res = res and True
    return res


def interleaveSeqs(a, b):
    assert len(a) == len(b)
    return ''.join(
        map(str, [x for t in zip(a, b) for x in t]))  # zip returns tuples. for x in t stuff flattens the tuples.


def e(x, n):
    # print("E of x:%s len:%s"%(x,len(x)))
    if len(x) == 3:
        print("implied decode x:%s" % x)
        return {'000': 0, '001': 1, '010': 2, '101': 3, '011': 4, '110': 5, '100': 6, '111': 7}[x]
    else:
        return deBruijnDecode(x, isqrt(n + 1) - 1)


def deBruijnConstruction(a, n, c, v):
    assert conditionA(a, n, v)
    b = '00' + a
    return interleaveSeqs(b * int(n / 2), a * int(1 + n / 2))


def deBruijnDecode(x, d):
    print("decode x:%s len:%s  size:%s" % (x, len(x), d))
    n = isqrt(d + 1) - 1
    print("n is %s," % n)
    y = x[0:len(x):2]
    z = x[1:len(x):2]
    assert x == interleaveSeqs(y, z)
    vmm = len(y)
    ey = e(y, d)
    ez = e(z, d)
    # print("eY %s  eZ %s"%(ey,ez))
    # 0**(len(x/2)) aka 0**v, is the longest possible zero vector, but A is a punctured deBruijn, so y=0**v means
    #       y is from B, not A. B starts with 0**(v+1), so the position of y is 0 or 1 in B, mod len(b)
    #       the mod is because B is repeated in D.
    if y == '0' * vmm:  # y is 0**v
        # q is 0 or 1, mod n+2
        # q is E(z) mod n
        # n = len(a); len(d) is n(n+2)
        # calc q. return 2q
        # print("Trivial Y=0 case")
        for i in range(0, n * (n + 2)):
            c1 = (i * (n + 2))
            c2 = (i * (n + 2)) + 1
            for j in range(i, n * (n + 2)):
                c3 = ez + i * n
                if c1 == c3:
                    return 2 * i
                if c2 == c3:
                    return 2 * i
    # Same basic logic as above, but this time it's z that is in b.
    if z == '0' * vmm:
        # print("Trivial Z=0 case")
        # q+1 is 0 or 1, mod n+2
        # q is E(y) mod n
        # return 2q+1
        for i in range(0, n * (n + 2)):
            c1 = (i * (n + 2))
            c2 = (i * (n + 2)) + 1
            for j in range(i, n * (n + 2)):
                c3 = ey + j * n
                if c1 == c3:
                    return 2 * i + 1
                if c2 == c3:
                    return 2 * i + 1
    # y and z are not 0**v, so we have slightly more complicated situations.
    if (ez - ey) % 2 == 0:
        # print ('non-trivial, even')
        # q is ey+2 mod n+2
        # q is ez mod n
        # return 2q
        for i in range(0, n * (n + 2)):
            c1 = ey + 2 + i * (n + 2)
            for j in range(i, n * (n + 2)):
                c3 = ez + j * n
                if c1 == c3:
                    return 2 * i
    else:
        # print ('non-trivial, odd')
        # q+1 is Ez+2 mod n+2
        # q is ey mod n
        # return 2q+1
        for i in range(0, n * (n + 2)):
            c1 = ez + 1 + i * (n + 2)
            for j in range(i, n * (n + 2)):
                c3 = ey + j * n
                if c1 == c3:
                    return 2 * i + 1


def initialdeBruijn():
    n = 6
    c = 2
    v = 3
    a = '001011'
    d = deBruijnConstruction(a, n, c, v)
    print(d)
    return len(d)


n = 48
c = 2
v = 6
a = '000001001101101001000101100011100101000011001111'
d = deBruijnConstruction(a, n, c, v)
print(d)
print(len(d))

for i in range(0, len(d) - 11):
    p = deBruijnDecode(d[i:i + 12], len(d))
    if p == i:
        print("i:%2s E(%s)=%s is good" % (str(i), str(d[i:i + 12]), str(p)))
    else:
        print("i:%2s E(%s)=%s is bad" % (str(i), str(d[i:i + 12]), str(p)))

print("BROKEN!!!!")
