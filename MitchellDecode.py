def modulosolver(right, rn, left, ln, orcase, debug=False):
    # I think something is broken here
    right = right % rn
    left = left % ln
    if debug:
        print("right m is {} modulo {}.".format(right, rn))
        print("left m is {} modulo {}.".format(left, ln))
    if orcase:
        lp = (left + 1) % ln
    else:
        lp = left
    result = -1
    for i in range(0, ln):
        aa = (right + i * rn) % ln
        if debug:
            print("m={} i={} aa={} left={}".format((right + i * rn) % int((ln * rn) / 2), i, aa, left))
        if (aa == left) or (aa == lp):
            result = (right + i * rn) % int((ln * rn) / 2)
            break
    return result

def MitchellT(v, debug=False):
    if v == 6:
        return 12
    else:
        if debug:
            print("T({}) is unknown.".format(v))
        return -1

def MitchellSp(v, debug=False):
    if v == 6:
        return 4
    else:
        if debug:
            print("Sp({}) is unknown.".format(v))
        return -1

def Ep(ex, sp, debug=False):
    epx = ex  # S is 0, so all ex's are going to be in S..S'
    if ex > 0:
        epx += 2
        if ex > sp:
            epx += 2
    return epx

def MitchellFp(x, debug=False):
    y = x[0::2]
    z = x[1::2]
    if debug:
        print("x={} y={} z={}".format(x, y, z))
    v = len(y)
    orcase = False
    trivs = [[0] * v, [1] * v]
    s = 0
    case = 4
    if y in trivs or z in trivs:
        if y == [0] * v:
            case = 0
            if debug:
                print("Y is [0]*v")
        if y == [1] * v:
            case = 1
            if debug:
                print("Y is [1]*v")
        if z == [0] * v:
            case = 2
            if debug:
                print("Z is [0]*v")
        if z == [1] * v:
            case = 3
            if debug:
                print("Z is [1]*v")
    if case in (2, 3, 4):
        ey = MitchellDecode(y, debug)
        if debug:
            print("E(y)={}".format(ey))
    if case in (0, 1, 4):
        ez = MitchellDecode(z, debug)
        if debug:
            print("E(z)={}".format(ez))
    if case in (1, 3, 4):
        sp = MitchellSp(2 * v, debug)
    if case == 4:
        isEven = ((ez - ey) % 2 == 0)
        if debug:
            print("isEven={}".format(isEven))
    if case in (0, 1):
        m1 = ez
        Fp = 0
    if case in (2, 3):
        m1 = ey
        Fp = 1
    if case == 0:
        m2 = s
        orcase = True
    if case == 1:
        m2 = sp + 2
        orcase = True
    if case == 2:
        m2 = s - 1
        orcase = True
    if case == 3:
        m2 = sp + 1
        orcase = True
    if case == 4:
        if isEven:
            m1 = ez
            m2 = Ep(ey, sp, debug)
            Fp = 0
            if debug:
                print("m1=E(z)={} m2=E'(y)={}".format(m1, m2))
        else:
            m1 = ey
            m2 = Ep(ez, sp, debug) - 1
            Fp = 1
            if debug:
                print("m1=E(y)={} m2=E'(z)-1={}".format(m1, m2))
    m = modulosolver(m1, 2 ** v - 2, m2, 2 ** v + 2, orcase, debug)
    if debug:
        print("equation solver m={}".format(m))
        print("... and F'={}".format(Fp))

    return Fp + 2 * m


def MitchellDecode(x, debug=False):
    if debug:
        print("X is {}".format(x))
    v = len(x)
    if debug:
        print("V is {}".format(v))

    if v > 3:
        assert v % 2 == 0
        t = MitchellT(v, debug)
        if x == [1, 0] * int(v / 2):
            F = t
            if debug:
                print("X is [1,0]*nn/2, F={}".format(F))

        elif x == [0, 1] * int(v / 2):
            F = t + 1
            if debug:
                print("X is [0,1]*n/2, F={}".format(F))
        else:
            Fp = MitchellFp(x, debug)
            F = Fp
            if Fp > t:
                F += 2
            if debug:
                print("General Case. Fp={}, t={}, F={}".format(Fp, t, F))

    else:
        ea = [[0, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 0], [1, 0, 0]]
        assert x in ea
        F = ea.index(x)
        if debug:
            print("v=3, E({})={}".format(x, F))
    return F


import Mitchell

if __name__ == '__main__':
    D = [i for i in Mitchell.gend(3, [0, 0, 0, 1, 0, 1, 1, 1])]
    DD = D * 2
    for x in range(62):
        xx = DD[x:x + 6]
        e = MitchellDecode(DD[x:x + 6])
        if x!=e:
            s="!!!"
        else:
            s=""
        print("{}: {} {}  {}".format(xx, x, e,s))
    #     if e != x:
    #         MitchellDecode(DD[x:x + 6], True)
    #         print(D)
    #         print(len(D))
    #         break
    # print("".join([str(i) for i in D]))
'''
2:2
3:6
4:14
5:30
6:62


cases:
    1: y=0              ez
    2: y=1
    3: z=0
    4: z=1
    5: isEven
    6: not isEven


'''
