from collections import defaultdict, namedtuple

def best2(sequence):
    """
    Given an RNA sequence, such as ACAGU, we can predict its secondary structure
       by tagging each nucleotide as (, ., or ). Each matching pair of () must be
       AU, GC, or GU (or their mirror symmetries: UA, GC, UG).
       We also assume pairs can _not_ cross each other.
       The following are valid structures for ACAGU:
    """
    trace = namedtuple("track", "count is_curr_matching pre count_pre")
    dp = defaultdict(lambda: trace(count=0, is_curr_matching=False, pre=float("inf"), count_pre=0))

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            if isPair(sequence[i], sequence[i + size - 1]):
                dp[(i, i + size - 1)] = trace(count=dp[(i + 1, i + size - 2)].count + 1,
                                              is_curr_matching=True,
                                              pre=float("inf"),
                                              count_pre=float("inf"))
            tmp = max([trace(count=dp[(i, i + j)].count + dp[(i + j + 1, i + size - 1)].count,
                             is_curr_matching=False,
                             pre=i + j,
                             count_pre=dp[(i, i + j)].count)
                                for j in xrange(size - 1)],
                        key=lambda x:(x[0], x[3])) # x[2] take larger (i + j)

            # key=lambda x:(x[0], -x[1]):  -x[1] means to take is_curr_matching=True over is_curr_matching=False
            dp[(i, i + size - 1)] = max(dp[(i, i + size - 1)], tmp, key=lambda x:(x[0], -x[1]))

    return back_trace(dp, len(sequence))

def best(sequence):
    """
    Given an RNA sequence, such as ACAGU, we can predict its secondary structure
       by tagging each nucleotide as (, ., or ). Each matching pair of () must be
       AU, GC, or GU (or their mirror symmetries: UA, GC, UG).
       We also assume pairs can _not_ cross each other.
       The following are valid structures for ACAGU:
    """
    trace = namedtuple("track", "count is_curr_matching pre")
    dp = defaultdict(lambda: trace(count=0, is_curr_matching=False, pre=float("inf")))

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            if isPair(sequence[i], sequence[i + size - 1]):
                dp[i, i + size - 1] = trace(count=dp[i + 1, i + size - 2].count + 1,
                                              is_curr_matching=True,
                                              pre=float("inf"))
            tmp = max([trace(count=dp[i, i + j].count + dp[i + j + 1, i + size - 1].count,
                             is_curr_matching=False,
                             pre=i + j)
                                for j in xrange(size - 1)],
                        key=lambda x:(x[0], x[2])) # x[2] take larger (i + j)

            # key=lambda x:(x[0], -x[1]):  -x[1] means to take is_curr_matching=True over is_curr_matching=False
            dp[i, i + size - 1] = max(dp[i, i + size - 1], tmp, key=lambda x:(x[0], -x[1]))

    return back_trace(dp, len(sequence))


def back_trace(dp, length):
    letters = ['.'] * length
    count = dp[(0, length - 1)].count
    _back(0, length - 1, dp, letters)
    return count, "".join(letters)


def _back(left, right, dp, letters):
    if left < right:
        count, is_curr_matching, pre = dp[(left, right)]
        if is_curr_matching:
            letters[left], letters[right] = '(', ')'
            _back(left + 1, right - 1, dp, letters)
        elif count > 0:
            _back(left, pre, dp, letters)
            _back(pre + 1, right, dp, letters)


def isPair(a, b):
    """
    check if a, b is a pair of AU, GC or UG
    """
    if (a == 'U' and b == 'A') or (a == 'A' and b == 'U'):
        return True
    elif (a == 'G' and b == 'C') or (a == 'C' and b == 'G'):
        return True
    elif (a == 'U' and b == 'G') or (a == 'G' and b == 'U'):
        return True
    else:
        return False


def total(sequence):
    """
    Total number of all possible structures
    """
    dp = defaultdict(lambda: 1)
    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            if isPair(sequence[i], sequence[i + size - 1]):
                dp[i, i + size - 1] = 2
            dp[i, i + size - 1] += dp[i + 1, i + size - 1] + dp[i, i + size - 2] - 2
    return dp[0, len(sequence) - 1]


if __name__ == '__main__':
    print best("ACAGU")
    print best("AUBBU")
    print best("AUCGUG")
    print best("UCAG")
    print best("AUCGUGAU")

    print total("ACAGU")
    print total("AUBBU")
    print total("AUCGUG")
    print total("UCAG")
    print total("AUCGUGAU")
