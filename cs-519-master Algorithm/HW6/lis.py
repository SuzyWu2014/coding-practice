def lis(string):
    """
    Longest (Strictly) Increasing Subsequence
       - input/output are lower-case strings:
    """
    d = dict()
    d[0] = (1, -1, True)
    for i in xrange(1, len(string)):
        vals = [(d[j][0] + 1, j, True) for j in xrange(i) if string[j] < string[i]]
        d[i] = max(vals) if len(vals) > 0 else (1, -1, True)

    return back_trace(string, d)


def back_trace(string, d):
    rst = []
    curr = len(string) - 1
    while curr > -1:
        _, pre, if_curr = d[curr]
        if if_curr:
            rst.append(string[curr])
        curr = pre

    return "".join(reversed(rst))


if __name__ == '__main__':
    print lis("aebbcg")
    print lis("zyx")
    print(lis(""))
    print(lis("aaaa"))
    print(lis("aabbaacfgs"))