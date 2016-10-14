from operator import itemgetter
import itertools
import random
import heapq

def sort(pairs):
    return sorted(sorted(pairs, key=itemgetter(1)), key=lambda x: x[0] + x[1])


def nbesta(a, b):
    """
    Given two lists A and B, each with n integers, return
    a sorted list C that contains the smallest n elements from AxB:
    ordering:  (x,y) < (x',y') iff. x+y < x'+y' or (x+y==x'+y' and y<y')
    n^2 log n^2
    """
    if a is None or b is None or len(a) != len(b):
        return
    pairs = [i for i in itertools.product(a, b)]
    pairs = sort(pairs)
    return pairs[:len(a)]


def nbestb(a, b):
    """
    enumerate all n^2 pairs, but use qselect from hw1.
    n^2
    """
    if a is None or b is None or len(a) != len(b):
        return
    pairs = [i for i in itertools.product(a, b)]
    nth_pair = quickselect(pairs, len(a) + 1)
    n_pairs = filter(lambda x: sum(x) < sum(nth_pair) or ( sum(x) == sum(nth_pair) and x[1] < nth_pair[1]), pairs)
    same_y_pairs = filter(lambda x: sum(x) == sum(nth_pair) and x[1] == nth_pair[1], pairs)
    return sort(n_pairs + same_y_pairs[:(len(a) - len(n_pairs))])


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
    """
    Dijkstra-style best-first, only enumerate O(n) (at most 2n) pairs.
    """
    if a is None or b is None or len(a) != len(b):
        return
    a, b = sorted(a), sorted(b)
    heap = [(a[0],b[0])]
    i, j = 0, 0
    curr_sum = a[0] + b[0]
    while 1:
        tmp_sum, y = sum(heap[0]),heap[0][1]
        if a[i] + a[j + 1] < a[i + 1] + a[j]:
            rst.append
    print rst


a, b = [4, 1, 5, 3], [2, 6, 3, 4]
# a, b = [1, 1, 1, 1], [1, 1, 1, 1]
print nbesta(a, b)
print nbestb(a, b)
print nbestc(a, b)