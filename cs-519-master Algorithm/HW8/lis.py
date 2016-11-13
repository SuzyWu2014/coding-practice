import collections


def lis(string):
    if len(string) == 0:
        return ""
    record = collections.namedtuple("record", "length pre")
    dp = {-1: record(length=0, pre=-1)}
    for i in xrange(len(string)):
        dp[i] = max([record(dp[j].length + 1, pre=j)
                    for j in xrange(-1, i)
                        if j == -1 or string[j] < string[i]])
    return back_trace(string, dp)


def back_trace(string, dp):
    res = []
    curr = max(dp, key=dp.get)
    while curr >= 0:
        res.append(string[curr])
        _, pre = dp[curr]
        curr = pre
    return "".join(reversed(res))


if __name__ == '__main__':
    print(lis("aebbcg"))
    print(lis("zyx"))
    print(lis("z"))
    print(lis("aaaa"))
    print(lis("aabbaacfgs"))
    print(lis("bacpsa"))
    print(lis("abcbcdfcfghhhhishuab"))
