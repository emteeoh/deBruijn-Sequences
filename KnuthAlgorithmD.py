from itertools import cycle




class alg_D:
    def __init__(self,n,a):
        self.n=n
        self.a=a

    def __iter__(self):
        return alg_D_iter(self.n,self.a)

class alg_D_iter:
    def __init__(self,n,a):
        self.n=n
        self.a=a
        self.g=self.deBruijnGenerator()
        self.c=0
        self.max = 4*n*n

    def __iter__(self):
        return self

    def deBruijnGenerator(self):
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


    def __next__(self):
        self.c+=1
        if self.c <=(self.max):
            print("__next__ {}".format(self.c))
            return next(self.g)
        else:
            raise StopIteration



if __name__ == "__main__":

    j=0
    for i in alg_D(2,[0,0,1,1]):
        print("{}: {}".format(j,i))
        j +=1
