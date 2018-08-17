from itertools import cycle, islice
from .coroutine import *


def start(wordsize,consumer):
    w=wordsize
    chain= consumer
    while w > 2:
        if w%2 == 0:
            w = int(w / 2)
            chain=coroutine.mitchellx2setup(w,chain)
        elif w%2 == 1:
            w -= 1
            chain = coroutine.knuthcoroutine(w,chain)
    coroutine.simpledeBruijn(chain)

