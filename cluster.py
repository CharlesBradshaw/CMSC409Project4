import random
from functools import partial

TRIES = 30
ITERS = 20

def sqdist(a, b):
    dist = sum((x-y)**2 for x,y in zip(a, b))
    return dist

def kMIter(vectors, k):
    n = len(vectors)
    means = random.sample(vectors, k)
    for iter in xrange(ITERS):
        nearest = map(lambda v: min((sqdist(v, means[i]), i) \
            for i in xrange(k))[1], vectors)
        if iter == ITERS-1:
            return (err, means, nearest)
        next = [[] for i in xrange(k)]
        err = 0
        for i, val in enumerate(nearest):
            next[val].append(vectors[i])
            err += sqdist(vectors[i], means[val])
        means = map(lambda l: tuple(sum(c)/float(len(c)) for c in zip(*l)), next)

def kMeans(vectors, k):
    vectors = map(lambda v: tuple(map(float, v)), vectors)
    best = min(map(lambda i: kMIter(vectors, k), xrange(TRIES)))
    return best