import math

def binary_de_bruijn(n):
    """
    binary de Bruijn sequence
    and subsequences of length n.
    """

    alphabet = '01'
    k = 2

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

def de_bruijn(alphabet,n):
    """
    binary de Bruijn sequence
    and subsequences of length n.
    """

    k = len(alphabet)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

binary = binary_de_bruijn(16)
print(len(binary))
quad = de_bruijn('ABCD',8)
print(len(quad))
octal = de_bruijn('ABCDEFGH',5)
print(len(octal))
hex = de_bruijn('0123456789ABCDEF',4)
print(len(hex))

print()
print(2**15)
print(4**8)
print(8**5)
print(16**4)

print()
print (math.log(20000,2))
print (math.log(20000,4))
print (math.log(20000,8))
print (math.log(20000,16))

print()
print (2**(math.ceil(math.log(20000,2))))
print (4**(math.ceil(math.log(20000,4))))
print (8**(math.ceil(math.log(20000,8))))
print (16**(math.ceil(math.log(20000,16))))
