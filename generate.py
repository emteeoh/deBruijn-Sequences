from KnuthAlgorithmR import knuthR
from MitchellGenerate import genDeBruijn
from MitchellGenerate import doublepuncture


class iterbruijn:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iterbruijn_iter(self.n)


class iterbruijn_iter:
    def __init__(self, n):
        if n % 2 == 0 and n > 2:
            halfn = int(n / 2)
            # print("Mitchell({})".format(halfn))
            self.a = genDeBruijn(halfn, iterbruijn(halfn))
        elif n % 2 == 1 and n > 3:
            prevn = n - 1
            # print("Knuth({})".format(prevn))
            self.a = knuthR( prevn, iterbruijn(prevn))
        elif n == 2:
            # print("Trivial n=2")
            self.a = iter([0, 0, 1, 1])
        else:  # n==3
                # if n is actually 1 or 0, this code just kinda assumes its 3. 1 and 0 are kinda meaningless/trivial deBruijns
            # print("Trivial n=3")
            self.a = iter([0, 0, 0, 1, 0, 1, 1, 1])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.a)
        except StopIteration:
            raise StopIteration

class iterdpdB:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return iterdpdB_iter(self.n)


class iterdpdB_iter:
    def __init__(self,v):
        self.count=2**v-2
        self.a=doublepuncture(v,iterbruijn(v))

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count >=0 :
            return next(self.a)
        else:
            raise StopIteration

if __name__ == "__main__":
    for i in [3,4,5,6,8]:
        print("{:4}: {}".format(i,[x for x in iterbruijn(i)]))
    print()
    for i in [3,4,5,6,8]:
        print("dp{:2}: {}".format(i,[x for x in iterdpdB(i)]))
