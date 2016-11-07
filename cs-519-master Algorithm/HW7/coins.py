from collections import defaultdict, namedtuple


# def best(V, coins):
#     record = namedtuple("record", ["count_type", "count_curr"])
#     dp = defaultdict(lambda : record(count_type=-1, count_curr=-1))
#     for i in xrange(len(coins)):
#         dp[0, i] = record(count_type=0, count_curr=0)
#     for v in xrange(1, V + 1):
#         for i, val in enumerate(coins):
#             tmp = filter(lambda x: x.count_type > -1,[record(dp[v - val * k, i - 1].count_type, k) for k in xrange(1, v // val)])
#             if tmp == []:
#                 dp[v, i] = record(dp[v, i - 1].count_type, 0)
#             else:
#                 dp[v, i] = record(min(map(lambda x: (x[0] + 1, x[1]), tmp)))
#                 print(dp[v, i])

# def best(V, coins):
#     dp = defaultdict(lambda : -1)
#     for i in xrange(len(coins) + 1):
#         dp[0, i] = (0, 0)
#     for v in xrange(1, V + 1):
#         for i, val in enumerate(coins):
#             pres = [(dp[v - val * k, i][0] + 1, k) for k in xrange(1, v // val) if dp[v - val * k, i] != -1]
#             if pres == []:
#                 dp[v, i + 1] = dp[v, i]
#             else:
#                 dp[v, i + 1] = min(pres)
#             print(dp)

def best(V, coins):
    dp = defaultdict(lambda :float("inf"))
    for i in xrange(-1, len(coins) + 1):
        dp[0, i] = 0
    for i in xrange(1, V + 1):
        dp[i, -1] = None
    for v in xrange(1, V + 1):
        for i, val in enumerate(coins):
            exclude = dp[v, i - 1]
            for k in xrange(1, (v // val) + 1):
                include = dp[v - val * k, i - 1]
                if include is not None:
                    dp[v, i] = min(dp[v, i], include + 1)
            if exclude is not None:
                dp[v, i] = min(exclude, dp[v, i])
            # print(v, i, dp[v, i])
            # include = filter(lambda x: x is not None,[dp[v - val * k, i - 1] for k in xrange(1, (v // val) + 1)])
    print(dp[V, len(coins) - 1])

if __name__ == '__main__':
    print(best(47, [6, 10, 15]))
    print(best(59, [6, 10, 15]))
    print(best(37, [4, 6, 15]))
    print(best(27, [4, 6, 15]))
    print(best(75, [4, 6, 15]))
