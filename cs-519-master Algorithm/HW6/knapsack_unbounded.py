import time
import random


def best(weight, items):
    """
    Unbounded Knapsack

    You have n items, each with weight w_i and value v_i, and has infinite copies.
    **All numbers are positive integers.**
    What's the best value for a bag of W?
    (0, -1) => max_val, index of current item
    """
    d = [(0, -1) for i in xrange(weight + 1)]
    for w in xrange(1, weight + 1):
        vals = [(d[w - wi][0] + vi, i) for i, (wi, vi) in enumerate(items) if w >= wi]
        d[w] = max(vals, key=lambda x: (x[0], -x[1])) if len(vals) > 0 else (0, -1)

    count = back_trace(weight, items, d)
    return (d[weight][0], count)


def back_trace(weight, items, d):
    count = [0 for i in xrange(len(items))]
    while weight > 0:
        item = d[weight][1]
        count[item] += 1
        weight -= items[item][0]
    return count


def best2(weight, items):
    d = dict()

    def _best(weight, d):
        if weight <= 0:
            d[0] = (0, -1)
            return d[0]
        if weight in d:
            return d[weight]

        vals = [(_best(weight - wi, d)[0] + vi, i) for i, (wi, vi) in enumerate(items) if weight >= wi ]
        d[weight] = max(vals, key=lambda x: (x[0], -x[1])) if len(vals) > 0 else (0, -1)
        return d[weight]

    max_val, _ = _best(weight, d)
    count = back_trace(weight, items, d)
    return (max_val, count)


if __name__ == '__main__':
    items = []
    for i in xrange(50):
        items.append((random.randint(0, 20),random.randint(0, 20)))
    time1 = time.time()
    print(best(32, items))
    elapse = time.time() - time1
    print(elapse)
    time1 = time.time()
    print(best2(32, items))
    elapse = time.time() - time1
    print(elapse)
    # print best(3, [(2, 4), (3, 5)])
    # print best(3, [(1, 5), (1, 5)])
    # print best(3, [(1, 2), (1, 5)])
    # print best(3, [(1, 2), (2, 5)])
    # print best(58, [(5, 9), (9, 18), (6, 12)])
    # print best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])

    # print best2(3, [(2, 4), (3, 5)])
    # print best2(3, [(1, 5), (1, 5)])
    # print best2(3, [(1, 2), (1, 5)])
    # print best2(3, [(1, 2), (2, 5)])
    # print best2(58, [(5, 9), (9, 18), (6, 12)])
    # print best2(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
