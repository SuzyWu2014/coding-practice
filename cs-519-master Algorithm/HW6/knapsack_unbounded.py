def best(weight, items):
    """
    Unbounded Knapsack

    You have n items, each with weight w_i and value v_i, and has infinite copies.
    **All numbers are positive integers.**
    What's the best value for a bag of W?
    """
    d = [(0, -1) for i in xrange(weight + 1)]

    for w in xrange(1, weight + 1):
        vals = [(d[w - item[0]][0] + item[1], i) for i, item in enumerate(items) if w >= item[0]]
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


# def best2(weight, items):
# pass


print best(3, [(2, 4), (3, 5)])
print best(3, [(1, 5), (1, 5)])
print best(3, [(1, 2), (1, 5)])
print best(3, [(1, 2), (2, 5)])
print best(58, [(5, 9), (9, 18), (6, 12)])
print best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
