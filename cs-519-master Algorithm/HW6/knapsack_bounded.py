import collections


def best(weight, items):
    if weight is None or items is None:
        return
    d = collections.defaultdict(dict)

    def _best(weight, item_index, d):
        if weight <= 0:
            d[0][item_index] = (0, item_index, 0)
            return d[0][item_index]
        if item_index == 0:
            d[weight][0] = (0, 0, 0)
            return d[weight][0]
        if weight in d and item_index in d[weight]:
            return d[weight][item_index]
        wi, vi, ci = items[item_index - 1]
        vals = [(_best(weight - wi * k, item_index - 1, d)[0] + vi * k, item_index, k) for k in xrange(1, ci + 1) if weight >= wi * k]
        tmp = max(vals, key=lambda x: (x[0], -x[1])) if len(vals) > 0 else (0, item_index, 0)
        d[weight][item_index] = max(_best(weight, item_index - 1, d), tmp, key=lambda x: (x[0], -x[1]))
        return d[weight][item_index]

    max_val, item, cp = _best(weight, len(items), d)
    return (max_val, back_trace(weight, items, d))


def best2(weight, items):
    """
    Bounded Knapsack

    You have n items, each with weight w_i and value v_i, and has c_i copies.
    **All numbers are positive integers.**
    What's the best value for a bag of W?
    (0, -1, -1): max_val, index of curr item, # of curr item
    """
    if weight is None or items is None:
        return
    if weight <= 0:
        return (0, [0] * len(items))
    d = [[0] * (len(items) + 1) for i in xrange(weight + 1)]
    for i in xrange(weight + 1):
        d[i][0] = (0, 0, 0)
    for i in xrange(len(items) + 1):
        d[0][i] = (0, i, 0)

    for w in xrange(1, weight + 1):
        for i, (wi, vi, ci) in enumerate(items):
            vals = [(d[w - wi * k][i][0] + vi * k, i + 1, k )
                        for k in xrange(1, ci + 1) if w >= wi * k]
            tmp = max(vals, key=lambda x: (x[0], -x[1])) if len(vals) > 0 else (0, i + 1, 0)
            d[w][i + 1] = max(d[w][i], tmp, key=lambda x: (x[0], -x[1]))

    return (d[weight][len(items)][0], back_trace(weight, items, d))


def back_trace(weight, items, d):
    rst = [0] * len(items)
    curr = len(items)
    while weight > 0 and curr > 0:
        _, curr, cnt = d[weight][curr]
        rst[curr - 1] = cnt
        weight -= items[curr - 1][0] * cnt
        curr -= 1
    return rst


if __name__ == '__main__':
    print(best(0, [(2, 4, 2), (3, 5, 3)]))
    print(best(-20, [(2, 4, 2), (3, 5, 3)]))
    print(best(2, [(2, 4, 2), (3, 5, 3)]))
    print(best(1, [(2, 4, 2), (3, 5, 3)]))
    print(best(5, []))
    print(best(5, None))
    print(best(5, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
