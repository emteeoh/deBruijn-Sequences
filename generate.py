import KnuthAlgorithmD
import KnuthAlgorithmR
import itertools


class deBruijnSequence:
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        return deBruijnSequence_iter(self.n)

class deBruijnSequence_iter:
    def __init__(self,n):
        if n > 3:
            if n%2 == 0:
                self.myiter=KnuthAlgorithmD.alg_D(n/2,deBruijnSequence(n/2))
                self.n=n/2
                lenN = 2 ** self.n ** 2
            else:
                self.myiter=KnuthAlgorithmR.alg_R(n-1,deBruijnSequence(n-1))
                self.n=n-1
        else:
            if n == 3:
                self.myiter=iter([ 0, 0, 0, 1, 0, 1, 1, 1])
                self.n = 9
            else:
                self.myiter=iter([ 0, 0, 1, 1 ])
                self.n = 5
        self.lenN = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.n = self.n - 1
        if self.n > 0:
            return self.myiter.__next__()
        else:
            raise StopIteration


if __name__ == "__main__":
    for i in deBruijnSequence(4):
        print(i)