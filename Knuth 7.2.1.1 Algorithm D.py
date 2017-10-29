from itertools import cycle



def alg_D(m,n,a):
    f=cycle(a)
    fp=cycle(a)
    x=xp=m
    y=t=yp=tp=0
    if (m%2)==0:
        r=2
    else:
        r=1
    goto = 'D3'
    while True:
        goto = 'D3'
        if (t!=n) or (x>=r):
            y=next(f)
        if (x!=y):
            x=y
            t=1
        else:
            t+=1
        while True:
            if goto == 'D3':
                yield x
            yp = next(fp)
            if (xp != yp):
                xp = yp
                tp =1
            else:
                tp += 1
            goto = 'D1'
            if (tp == n) and (xp < r):
                if (t<n) or (xp<x):
                    goto = 'D4'
            if (tp ==n) and (xp <r) and (xp==x) and (goto == 'D1'):
                    goto = 'D3'
            if goto =='D1':
                yield xp
                if (tp == n)and(xp<r):
                    goto='D3'
            if goto == 'D1':
                break


if __name__ == "__main__":
    from deBruijn import deBruijnBinary2bit
    m=2
    n=2
    a=deBruijnBinary2bit
    ad=alg_D(m,n,a)
    b=[]
    for j in range(m**(n*2)):
        b.append(next(ad))
    print("{}: {} {} ".format(n*2, len(b), b))