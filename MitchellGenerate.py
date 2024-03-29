from itertools import cycle


def puncture(n, a):
    ac = cycle(a)
    lookback = [3] * (n - 1)
    while True:
        nn = next(ac)
        if lookback == [0] * (n - 1) and nn == 0:
            nn = next(ac)
        lookback.pop(0)
        lookback.append(nn)
        yield nn


def doublepuncture(n, a):
    ac = puncture(n, a)
    lookback = [3] * (n - 1)
    while True:
        nn = next(ac)
        if lookback == [1] * (n - 1) and nn == 1:
            nn = next(ac)
        lookback.pop(0)
        lookback.append(nn)
        yield nn


def enhance(n, a):
    ac = cycle(a)
    lookback = [3] * n
    count = 0
    while True:
        nn = next(ac)
        if lookback == [0] * n:
            yield 0
        if lookback == [1] * n:
            yield 1
        lookback.pop(0)
        lookback.append(nn)
        yield nn
        count += 1


# noinspection PyShadowingNames
def gendp(n, a):
    # create a d' for a 2n-window deBruijn
    ap = doublepuncture(n, a)  # a, punctured
    be = enhance(n, a)  # b is a, enhanced.
    lena = 2 ** n  # can't do a len() of a generator, so I calculate it instead.
    n2 = int(((lena - 2) * (lena + 2)) / 2)
    for i in range(n2):
        yield (next(be))
        yield (next(ap))
    raise StopIteration


def gend(n, a):
    ap = gendp(n, a)
    lookback = [3] * (2 * n - 1)
    while True:
        try:
            nn = next(ap)
        except StopIteration:
            raise StopIteration
        # print("lookback:{}".format(lookback))
        if lookback == ([1, 0] * (n - 1) + [1]):
            yield 0
            yield 1
        lookback.pop(0)
        lookback.append(nn)
        yield nn


# noinspection PyPep8Naming
def genDeBruijn(n, a):
    ap = gend(n, a)
    lookback = [3] * (2 * n - 1)
    while True:
        try:
            nn = next(ap)
        except StopIteration:
            raise StopIteration
        if lookback == [0] * (2 * n - 1):
            yield 0
        if lookback == [1] * (2 * n - 1):
            yield 1
        lookback.pop(0)
        lookback.append(nn)
        yield nn


if __name__ == "__main__":
    for i in gend(3, [0, 0, 0, 1, 0, 1, 1, 1]):
        print(i, end='')
    print()
    for i in genDeBruijn(4, [0, 0, 0, 1, 0, 1, 1, 1]):
        print(i, end='')
    print()
