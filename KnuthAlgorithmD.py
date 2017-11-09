from itertools import cycle

class alg_D:
    def __init__(self,n,a):
        self.n=n
        self.a=a

    def __iter__(self):
        return alg_D_iter(self.n)

class alg_D_iter:
    def __init__(self,n,a):
        self.n=n
        self.a=a

    def __iter__(self):
        return self

    def __next__(self):
        self.f = cycle(self.a)
        self.fp = cycle(self.a)
        self.x = self.xp = 2
        self.y = self.t = self.yp = self.tp = 0
        self.r = 2
        self.goto = 'D3'
        while True:
            self.goto = 'D3'
            if (self.t != self.n) or (self.x >= self.r):
                self.y = next(self.f)
            if (self.x != self.y):
                self.x = self.y
                self.t = 1
            else:
                self.t += 1
            while True:
                if self.goto == 'D3':
                    yield self.x
                self.yp = next(self.fp)
                if (self.xp != self.yp):
                    self.xp = self.yp
                    self.tp = 1
                else:
                    self.tp += 1
                goto = 'D1'
                if (self.tp == self.n) and (self.xp < self.r):
                    if (self.t < self.n) or (self.xp < self.x):
                        self.goto = 'D4'
                if (self.tp == self.n) and (self.xp < self.r) and (self.xp == self.x) and (self.goto == 'D1'):
                    self.goto = 'D3'
                if self.goto == 'D1':
                    yield self.xp
                    if (self.tp == self.n) and (self.xp < self.r):
                        self.goto = 'D3'
                if self.goto == 'D1':
                    break




if __name__ == "__main__":
    from deBruijn import deBruijnBinary2bit
    m=2
    n=2
    a=deBruijnBinary2bit
    ad=alg_D_iter(n,a)
    b=[]
    for j in range(m**(n*2)):
        b.append(ad.__next__())
    print("{}: {} {} ".format(n*2, len(b), b))