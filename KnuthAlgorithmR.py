from itertools import cycle

# Algorithm R will create a period n+1 deBruijn from a period n sequence.
# A is the period n sequence
# m is the size of the alphabet.
# I hope its obvious that n is n.

def alg_R(m,n,a):
    f=cycle(a)
    x=y=t=0
    skipf=False
    while True:
        yield x
        if x!=0 and t>=n:
            skipf=True
        while True:
            if not skipf:
                y=next(f)
            if y==1:
                t+=1
            else:
                t=0
            if (t==n and x != 0):
                skipf = False
            else:
                break
        skipf = False
        x = (x+y)%m


if __name__ == "__main__":
    # This stuff is just smoke tests. If the file is used as a module, this code won't be used and won't be missed.
    from deBruijn import deBruijnBinary2bit

    m=3
    n=2
    a=[0,0,1,1,0,2,1,2,2]
    aR=alg_R(m,n,a)
    out=''
    for i in range(m**(n+1)):
        out=out+str(next(aR))
    print(out)


    a=deBruijnBinary2bit
    for i in range(2,16):
        m=2
        n=i
        b=[]
        aR = alg_R(m, n, a)
        for j in range(m**(n+1)):
            b.append(next(aR))
        print("{}: {} {} ".format(i+1,len(b),b))
        a=b