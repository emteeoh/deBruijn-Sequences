from KnuthAlgorithmR import knuthR
from Mitchell import genDeBruijn


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


if __name__ == "__main__":
    for i in [3,4,5,6,8,16]:
        print("{:2}: ".format(i),end='')
        y = [ x for x in iterbruijn(i) ]
        print(y)