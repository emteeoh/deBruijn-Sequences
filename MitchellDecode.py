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


MitchellT = {3: 7, 4: 15, 6: 12, 8: 196, 16: 16764}

MitchellSp = {3: 4, 4: 6, 6: 34, 8: 124, 16: 32762}

BetelU = {2: 2, 3: 5, 4: 7, 5: 17, 6: 35}

# 3: 001011
# 4: 00010 01110 1011

MitchellE = {2: {(0, 0): 0, (0, 1): 1, (1, 0): 3, (1, 1): 2},
             3: {(0, 0, 1): 0, (0, 1, 0): 1, (0, 1, 1): 3, (1, 0, 0): 5, (1, 0, 1): 2, (1, 1, 0): 4},
             4: {(0, 0, 0, 1): 0, (0, 0, 1, 0): 1, (0, 0, 1, 1): 4, (0, 1, 0, 0): 2, (0, 1, 0, 1): 9, (0, 1, 1, 0): 11,
                 (0, 1, 1, 1): 5,
                 (1, 0, 0, 0): 13, (1, 0, 0, 1): 3, (1, 0, 1, 0): 8, (1, 0, 1, 1): 10, (1, 1, 0, 0): 12,
                 (1, 1, 0, 1): 7, (1, 1, 1, 0): 6}
             }


# noinspection PyUnusedLocal,PyPep8Naming
def Ep(ex, sp, debug=False):
    epx = ex + 2  # S is 0, so all ex's are going to be in S..S'
    if ex >= sp:
        epx += 2
    return epx


# noinspection PyUnboundLocalVariable,PyPep8Naming,PyPep8Naming,PyShadowingNames
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
        sp = MitchellSp[v]
        if debug:
            print("s' is {}".format(sp))
    if case == 4:
        isEven = ((ez - ey) % 2 == 0)
        if debug:
            print("isEven={}".format(isEven))
    if case in (0, 1):
        m1 = ez
        # noinspection PyPep8Naming
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
    # noinspection PyUnboundLocalVariable
    m = modulosolver(m1, 2 ** v - 2, m2, 2 ** v + 2, orcase, debug)
    if debug:
        print("equation solver m={}".format(m))
        print("... and F'={}".format(Fp))

    return Fp + 2 * m


def MitchellF(x,debug=False):
    v=len(x)
    if x==[1, 0]*int(v/2):
        F=MitchellT[v]
    elif x==[0,1]*int(v/2):
        F=MitchellT[v]+1
    else:
        F=MitchellFp(x,debug)
        if F >= MitchellT[v]:
            F+=2
    return F

# noinspection PyShadowingNames,PyPep8Naming
def MitchellDecode(x, debug=False):
    if debug:
        print("X is {}".format(x))
    v = len(x)
    if debug:
        print("V is {}".format(v))

    if v > 4:
        F=MitchellF(x,debug)
    else:
        F = MitchellE[v][tuple(x)]
        if debug:
            print("v=3, E({})={}".format(x, F))
    return F

def deBruijnEvenDecode(x,debug=False):
    v = len (x)
    if x == [0]*v:
        P=0
    elif x == [1]*v:
        P=BetelU[v]
    else:
        P= MitchellDecode(x)+1
        a=max(BetelU[v],MitchellT[v])
        b=min(BetelU[v],MitchellT[v])
        if b <= P < a:
            P+=1
        if P > a:
            P+=2
        # if P >= BetelU[v] and P > MitchellT[v]:
        #     P+=1
    if debug:
        print("debug",x, v, P, BetelU[v], MitchellT[v])
    return P

if __name__ == '__main__':
    # for i in MitchellE.keys():
    #     for j in MitchellE[i].keys():
    #         print("{}: {} {}".format(j,MitchellE[i][j],MitchellDecode(j)))
    #
    # D3=[0,0,0,1,0,1,1,1,0,0]
    # for i in range(8):
    #     j=deBruijnEvenDecode(D3[i:i + 3])
    #     if i != j:
    #         print("{}: {} {}".format(D3[i:i+3],i,deBruijnEvenDecode(D3[i:i+3])))
    print("Testing D4")
    good=True
    D4=[0,0,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0]
    for i in range(14):
        j=MitchellDecode(D4[i:i + 4])
        if i != j:
            print("{}: {} {}".format(D4[i:i+4],i,deBruijnEvenDecode(D4[i:i+4])))
            good=False
            break
    if not good:
        print("D4 broken...")
        raise Exception
    # # D5=[0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0]
    # D6=[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1,0,0,0,0,0]
    # for i in range(64):
    #     j=deBruijnEvenDecode(D6[i:i + 6])
    #     if i != j:
    #         print("{}: {} {}".format(D6[i:i + 6], i, j))
    #
    # print ("foo")
    print("Testing D6")
    D6=[0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1,0,0,0,0,0,0]
    for i in range(62):
        j=MitchellDecode(D6[i:i + 6])
        if i != j:
            print("{}: {} {}".format(D6[i:i + 6], i, j))
            good=False
            break
    if not good:
        print("D6 broken...")
        raise Exception
    print("Testing D8")
    D8 = [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    for i in range(254):
        j=MitchellDecode(D8[i:i + 8])
        if i != j:
            print("{}: {} {}".format(D8[i:i + 8], i, j))
            good=False
            break
    if not good:
        print("D8 broken...")
        raise Exception
    # print("Testing D16")
    # for i in range(65534):
    #     j=MitchellDecode(D16[i:i + 16])
    #     if i != j:
    #         print("{}: {} {}".format(D16[i:i + 16], i, j))
    #         good=False
    #         break
    # if not good:
    #     print("D16 broken...")
    #     raise Exception