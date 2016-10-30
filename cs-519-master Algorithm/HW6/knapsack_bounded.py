def best(weight, items):
    """
    Bounded Knapsack

    You have n items, each with weight w_i and value v_i, and has c_i copies.
    **All numbers are positive integers.**
    What's the best value for a bag of W?
    (0, -1, -1): max_val, index of curr item, # of curr item
    """
    d = [(0, -1, -1) for i in xrange(weight + 1)]
    for w in xrange(1, weight + 1):
        for i, (wi, vi, ci) in enumerate(items):
            vals = [(d[w - wi * k][0] + vi * k, i, k)
                        for k in xrange(1, ci + 1) if w >= wi * k]
            d[w] = max(max(d), max(vals, key=lambda x: (x[0], -x[1])) if len(vals) > 0 else (0, -1, -1))
    print(d[weight])



print best(3, [(2, 4, 2), (3, 5, 3)])
print best(3, [(1, 5, 2), (1, 5, 3)])
print(best(3, [(1, 5, 1), (1, 5, 3)]))
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
