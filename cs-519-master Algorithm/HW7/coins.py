from collections import defaultdict, namedtuple


def best(V, coins):
    record = namedtuple("record", ["count_type", "count_curr"])
    dp = defaultdict(lambda : record(count_type=float("inf"), count_curr=-1))
    for i in xrange(-1, len(coins) + 1):
        dp[0, i] = record(count_type=0, count_curr=0)
    for i in xrange(1, V + 1):
        dp[i, -1] = None
    for v in xrange(1, V + 1):
        for i, val in enumerate(coins):
            exclude = dp[v, i - 1]
            include = [record(dp[v - val * k, i - 1].count_type + 1, k)
                            for k in xrange(1, (v // val) + 1)
                                if dp[v - val * k, i - 1] is not None]

            dp[v, i] = min(include) if include != [] else dp[v, i]
            if exclude is not None:
                dp[v, i] = min(exclude, dp[v, i])
    return None if dp[V, len(coins) - 1] == (float("inf"), -1) else (dp[V, len(coins) - 1][0], backtrace(V, coins, dp))


def backtrace(V, coins, dp):
    count = [0] * len(coins)
    v, curr = V, len(coins) - 1
    while v > 0:
        _, cnt_curr = dp[v, curr]
        count[curr] = cnt_curr
        v -= coins[curr] * cnt_curr
        curr -= 1
    return count


if __name__ == '__main__':
    print(best(47, [6, 10, 15]))
    print(best(59, [6, 10, 15]))
    print(best(37, [4, 6, 15]))
    print(best(27, [4, 6, 15]))
    print(best(75, [4, 6, 15]))
    print(best(17, [2, 4, 6]))
