def num_yes(num):
    """
    Number of bit strings of length n that has
    - two consecutive 0s.

    - 1 **** dp[i - 1]
    - 01**** dp[i - 2]
    - 00 *** pow(2, i - 2)
    """
    if num <= 1:
        return 0
    dp = [0, 0, 1]
    for i in xrange(3, num + 1):
        dp.append(dp[i - 1] + dp[i - 2] + pow(2, i - 2))
    return dp[num]


def num_no(num):
    return pow(2, num) - num_yes(num)

if __name__ == '__main__':
    print(num_yes(3))
    print(num_yes(4))
    print(num_no(3))
    print(num_no(4))
