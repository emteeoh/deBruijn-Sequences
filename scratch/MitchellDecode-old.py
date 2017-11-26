import MitchellGenerate

def MitchellT(n):
    if n==3:
        return 12
    else:
        return -1

def MitchellSP(n):
    if n==3:
        return 4
    else:
        return -1

def MitchellOnes(n):
    if n==3:
        return 34
    else:
        return -1

def modulosolver(right, rn, left, ln, orcase):
    if orcase:
        lp=(left+1)%ln
    else:
        lp = left
    result=-1
    for i in range(0, ln):
        aa = (right + i * rn) % ln
        if (aa == left) or (aa == lp):
            result=(right + i * rn)
            break
    return result

def inTP(x):
    v=len(x)
    notTP = [[0]*v, [1]*v, [0,1]*(v/2), [1,0]*(v/2)]
    if x in notTP:
        return False
    else:
        return True

def E(x, debug=False):
    if len(x)==3:
        ea=[[0,0,1],[0,1,0],[1,0,1],[0,1,1],[1,1,0],[1,0,0]]
        if debug:
            print(x)
            print (ea.index(x))
        return ea.index(x)
    else:
        MitchellDecode(x)

def MitchellDecode(x,debug=False):
    assert len(x) % 2 == 0
    n=len(x)
    assert n % 2 == 0
    xtrivials=[[0]*n,[1]*n,[0,1]*int(n/2),[1,0]*int(n/2)]
    t = MitchellT(int(n/2))
    if debug:
        print("t:{}".format(t))
    fp=0
    if
    try:
        casex = xtrivials.index(x)
        if casex == 0:
            f=0
            if debug:
                print("X is 0000...")
        if casex == 1:
            f=MitchellOnes(int(n/2))
            if debug:
                print("X is 111111...")
        if casex == 2:
            f=t+2
            if debug:
                print("X is 0101...")
        if casex == 3:
            f=t
            if debug:
                print("X is 1010...")
    except ValueError:
        y=x[0::2]
        z=x[1::2]
        n=len(y)
        sp=MitchellSP(n)
        if debug:
            print("S':{}".format(sp))
        assert len(z) == n
        trivials = [[0]*n,[1]*n,[0,1]*int(n/2),[1,0]*int(n/2)]
        orcase=False
        try:
            casey=trivials.index(y)
            if debug:
                print("y is a trivial")

        except ValueError:
            casey=-1
        try:
            casez=trivials.index(z)
            if debug:
                print("z is a trivial")
        except ValueError:
            casez=-1
        leftm=0
        ey=ez=0
        if casey != 0:
            ey = E(y)
            epy =ey + 2
            if ey > sp:
                epy += 2
            leftm = epy
            isEven =

        if casez != 0:
            ez = E(z)
            epz =ez + 2
            if ez > sp:
                epz+=2
        if debug:
            print("E(y):{} E(z):{} E'(y):{} E'(z):{}".format(ey,ez,epy,epz))
        isEven = ((ez-ey)%2) == 0
        if (casey==0) or (casey==1) or isEven:
            rightm=ez
            fp=0
            if debug:
                print("Y is 0, 1, or isEven")
        elif (casez==0) or (casez==1) or not isEven:
            rightm=ey
            fp=1
            if debug:
                print("Z is 0, 1, or not isEven, using right=E(y)")
        if casey==0:
            leftm=0 # or 1
            orcase=True
            if debug:
                print("Y is 0, left=0 or 1")
        elif casey==1:
            leftm=sp+2 # or +3
            orcase=True
            if debug:
                print("Y is 1, left=sp or sp+1")
        elif casez==0:
            leftm = -1
            orcase=True
            if debug:
                print("Z is 0, left=sp-1 or sp")
        elif casez==1:
            leftm = sp+1
            orcase=True
            if debug:
                print("Z is 1, left=sp+1 or sp+2")
        elif isEven:
            leftm = epy
            if debug:
                print("isEven, using E'(y)")
        else:
            leftm = epz - 1
            if debug:
                print("not isEven, using E'(z)-1")
        m = modulosolver(leftm, n, rightm, n + 4,orcase)
        if debug:
            print("left:{} right:{} orcase:{} m:{} fp:{}".format(leftm,rightm,orcase,m,fp))
        fp+=2*m
        f=fp
        if fp >= t:
            if debug:
                print("isEven, E(y) > sp")
            f+=2
    return f

def bruteforceit(D,x):
    l = len(x)
    for i in range(len(D)):
        if x == D[i:i+l]:
            return i

#print(MitchellDecode([1,0,0,1,1,0],True))
D=[]
for i in MitchellGenerate.gend(3, [0, 0, 0, 1, 0, 1, 1, 1]):
    D.append(i)
print(D, len(D))

for i in range(len(D)):
    x=(D+D)[i:i+6]
    print(i,x,bruteforceit(D,x),MitchellDecode(x))
""

001
010
101
011
110

