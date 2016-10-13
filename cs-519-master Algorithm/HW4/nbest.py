from operator import itemgetter
import itertools
import random

def sort(pairs):
    return sorted(sorted(pairs, key=itemgetter(1)), key=lambda x: x[0] + x[1])


def nbesta(a, b):
    """
    Given two lists A and B, each with n integers, return
    a sorted list C that contains the smallest n elements from AxB:
    ordering:  (x,y) < (x',y') iff. x+y < x'+y' or (x+y==x'+y' and y<y')
    n^2 log n^2
    """
    pairs = [i for i in itertools.product(a, b)]
    pairs = sort(pairs)
    return pairs[:len(a)]


def nbestb(a, b):
    """
    n^2
    """
    pairs = [i for i in itertools.product(a, b)]
    nth_pair = quickselect(pairs, len(a) + 1)
    n_pairs = filter(lambda x: sum(x) < sum(nth_pair) or ( sum(x) == sum(nth_pair) and x[1] < nth_pair[1]), pairs)
    return sort(n_pairs)


def quickselect(pairs, k):
    if k <= 0 or pairs is None or k > len(pairs):
        return
    pair = random.choice(pairs)
    left = filter(lambda x: sum(x) < sum(pair) or (sum(x) == sum(pair) and x[1] < pair[1]), pairs)
    right = filter(lambda x: sum(x) > sum(pair) or (sum(x) == sum(pair) and x[1] > pair[1]), pairs)
    if k <= len(left):
        return quickselect(left, k)
    elif k > len(pairs) - len(right):
        return quickselect(right, k - (len(pairs) - len(right)))
    else:
        return pair

def nbestc(a, b):
    pass

a, b = [4, 1, 5, 3], [2, 6, 3, 4]
print nbesta(a, b)
print nbestb(a, b)