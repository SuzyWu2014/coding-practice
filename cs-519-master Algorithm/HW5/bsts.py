def bsts(num):
    """
    Number of n-node BSTs
    input: n
    output: number of n-node BSTs

    dp[k] = sum(dp[i] * dp[k - i])
    """
    if num <= 0:
        return 0
    if num <= 2:
        return num
    dp = [0] * (num + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for k in xrange(3, num + 1):
        count = 0
        for i in xrange(k):
            count += dp[i] * dp[k - i - 1]
        dp[k] = count
    return dp[num]


if __name__ == '__main__':
    print(bsts(3))
    print(bsts(4))
    print(bsts(5))