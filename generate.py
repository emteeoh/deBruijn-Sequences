from KnuthAlgorithmR import alg_R
from Mitchell import genDeBruijn


class iterbruijn:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iterbruijn_iter(self.n)


class iterbruijn_iter:
    def __init__(self, n):
        self.n = n
        if self.n % 2 == 0 and n > 2:
            halfn = int(n / 2)
            self.a = genDeBruijn(halfn, iterbruijn(halfn))
        elif self.n % 2 == 1 and n > 3:
            prevn = n - 1
            self.a = alg_R(2, prevn, iterbruijn(prevn))
        elif n == 2:
            self.a = iter([0, 0, 1, 1])
        else:  # n==3
            self.a = ([0, 0, 0, 1, 0, 1, 1, 1])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.a)


if __name__ == "__main__":
    for i in iterbruijn(4):
        print(i,end='')
    print("\n")
    for i in iterbruijn(5):
        print(i,end='')
