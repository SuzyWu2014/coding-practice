from collections import defaultdict, namedtuple


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
            dp[i, i + size - 1] = max(dp[i, i + size - 1], tmp)

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
    GCAC G
    0123 4
    """
    dp = defaultdict(int)
    for i in xrange(len(sequence)):
        dp[i, i] = 1
        dp[i, i - 1] = 1

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            if isPair(sequence[i], sequence[i + size - 1]):
                dp[i, i + size - 1] += dp[i + 1, i + size - 2]
            dp[i, i + size - 1] += dp[i, i + size - 2]
            for k in xrange(i + 1, i + size - 1):
                if isPair(sequence[i + size - 1], sequence[k]):
                    dp[i, i + size - 1] += dp[i, k - 1] * dp[k + 1, i + size - 2]

    return dp[0, len(sequence) - 1]

def kbest(sequence, k):
    """
    Given an RNA sequence, such as ACAGU, we can predict its secondary structure
       by tagging each nucleotide as (, ., or ). Each matching pair of () must be
       AU, GC, or GU (or their mirror symmetries: UA, GC, UG).
       We also assume pairs can _not_ cross each other.
       The following are valid structures for ACAGU:
    """
    trace = namedtuple("track", "count is_curr_matching pre")
    dp = defaultdict(set)
    # lambda: trace(count=0, is_curr_matching=False, pre=float("inf"))
    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            if isPair(sequence[i], sequence[i + size - 1]):
                dp[i, i + size - 1].add(trace(count=dp[i + 1, i + size - 2][0].count + 1,
                                              is_curr_matching=True,
                                              pre=float("inf")))
            tmp = max([trace(count=dp[i, i + j].count + dp[i + j + 1, i + size - 1].count,
                             is_curr_matching=False,
                             pre=i + j)
                                for j in xrange(size - 1)],
                        key=lambda x:(x[0], x[2])) # x[2] take larger (i + j)

            # key=lambda x:(x[0], -x[1]):  -x[1] means to take is_curr_matching=True over is_curr_matching=False
            dp[i, i + size - 1] = max(dp[i, i + size - 1], tmp)

    return back_trace(dp, len(sequence))

if __name__ == '__main__':
    # print best("UUCAGGA")
    # print best("GUUAGAGUCU")
    # print best("GCACG")
    # print best("AUAACCUUAUAGGGCUCUG")
    # print best("UUGGACUUGAGAAAAG")
    # print best("UCAAUGGGUAGUAAAU")
    # print best("UUUGGCACUUUCAGA")
    # print best("ACACACCUUGUCCGUGAA")
    # print best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG")
    # print best("CGCGAAUAAAAAGGCACUGUU")
    # print best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC")
    # print best("UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU")
    # print best("AUACGUCGGGGACAAGAAUUACGG")
    # print best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
    # print best("CGAGGUGGCACUGACCAAACACCACCGAAAC")
    # print best("CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU")
    # print best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")
    # print best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")

    print best("ACAGU")
    print total("ACAGU")

    print best("AC")
    print total("AC")

    print best("GUAC")
    print total("GUAC")

    print best("GCACG")
    print total("GCACG")

    print best("CCGG")
    print total("CCGG")

    print best("CCCGGG")
    print total("CCCGGG")

    print best("UUCAGGA")
    print total("UUCAGGA")

    print best("AUAACCUA")
    print total("AUAACCUA")

    # print total("GUUAGAGUCU")

    print best("UUGGACUUG")
    print total("UUGGACUUG")

    print best("UUUGGCACUA")
    print total("UUUGGCACUA")

    print best("GAUGCCGUGUAGUCCAAAGACUUC")
    print total("GAUGCCGUGUAGUCCAAAGACUUC")

    print best("AGGCAUCAAACCCUGCAUGGGAGCG")
    print total("AGGCAUCAAACCCUGCAUGGGAGCG")
