import coroutines



def simpledeBruijn(nextcoroutine):
    a=[0,0,1,1]
    coroutines.cycleProducer(a,nextcoroutine)

@coroutines.coroutine
def puncture(wordsize, nextcoroutine):
    lookback = [3] * (wordsize - 1)
    try:
        while True:
            nn = (yield)
            if lookback == [0] * (wordsize - 1) and nn == 0:
                nn = (yield)
            lookback.pop(0)
            lookback.append(nn)
            nextcoroutine.send(nn)
    except GeneratorExit:
        nextcoroutine.close()

@coroutines.coroutine
def doublepuncture(wordsize, nextcoroutine):
    lookback = [3] * (wordsize - 1)
    try:
        while True:
            nn = (yield)
            if lookback == [1] * (wordsize - 1) and nn == 1:
                nn = (yield)
            lookback.pop(0)
            lookback.append(nn)
            nextcoroutine.send(nn)
    except GeneratorExit:
        nextcoroutine.close()

@coroutines.coroutine
def enhance(wordsize, nextcoroutine):
    lookback = [3] * wordsize
    while True:
        nn = yield
        if lookback == [0] * wordsize:
            nextcoroutine.send(0)
        if lookback == [1] * wordsize:
            nextcoroutine.send(1)
        lookback.pop(0)
        lookback.append(nn)
        nextcoroutine.send(nn)



def gendp(wordsize,nextcoroutine):
    # create a d' for a 2n-window deBruijn
    c=coroutines.combine(2,nextcoroutine)
    return (c.receiver(0),c.receiver(1))

@coroutines.coroutine
def gend(wordsize, nextcoroutine):
    # find the 1010...1 section and add 01 to it.
    lookback = [3] * (2 * wordsize - 1)
    while True:
        nn = yield
        if lookback == ([1, 0] * (wordsize - 1) + [1]):
            nextcoroutine.send(0)
            nextcoroutine.send(1)
        lookback.pop(0)
        lookback.append(nn)
        nextcoroutine.send(nn)

@coroutines.coroutine
def genmitchell(wordsize, nextcoroutine):
    # find the 000... and 111... sections and expand them by one bit.
    lookback = [3] * (2 * wordsize - 1)
    while True:
        nn = yield
        if lookback == [0] * (2 * wordsize - 1):
            nextcoroutine.send(0)
        if lookback == [1] * (2 * wordsize - 1):
            nextcoroutine.send(1)
        lookback.pop(0)
        lookback.append(nn)
        nextcoroutine.send(nn)

def mitchellx2setup(wordsize,nextcoroutine):
    chain = genmitchell(wordsize,nextcoroutine)
    chain = gend(wordsize,chain)
    c1,c2 = gendp(wordsize,chain)
    c1 = enhance(wordsize,c1)
    c2 = doublepuncture(wordsize,c2)
    c2 = puncture(wordsize,c2)
    chain = coroutines.split(c1,c2)
    return chain

@coroutines.coroutine
def knuthcoroutine(wordsize,nextcoroutine):
    x = y = t = 0
    skipf = False
    try:
        while True:
            nextcoroutine.send(x)
            if x != 0 and t >= wordsize:
                skipf = True
            while True:
                if not skipf:
                    y = (yield)
                if y == 1:
                    t += 1
                else:
                    t = 0
                if (t == wordsize and x != 0):
                    skipf = False
                else:
                    break
            skipf = False
            x = (x + y) % 2
    except StopIteration:
        pass



