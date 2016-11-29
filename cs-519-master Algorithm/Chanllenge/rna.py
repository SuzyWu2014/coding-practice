from collections import defaultdict, namedtuple
import heapq


def best(sequence):
    """
    Given an RNA sequence, such as ACAGU, we can predict its secondary structure
       by tagging each nucleotide as (, ., or ). Each matching pair of () must be
       AU, GC, or GU (or their mirror symmetries: UA, GC, UG).
       We also assume pairs can _not_ cross each other.
       The following are valid structures for ACAGU:
    """
    trace = namedtuple("trace", "count is_curr_matching pre")
    pair = defaultdict(lambda: trace(count=0, is_curr_matching=False, pre=float("inf")))

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            j = i + size - 1
            if isPair(sequence[i], sequence[j]):
                pair[i, j] = trace(count=pair[i + 1, j - 1].count + 1,
                                              is_curr_matching=True,
                                              pre=float("inf"))
            tmp = max([trace(count=pair[i, t].count + pair[t + 1, j].count,
                             is_curr_matching=False,
                             pre=t)
                                for t in xrange(i, j)],
                        key=lambda x:(x[0], x[2])) # x[2] take larger (i + j)

            # key=lambda x:(x[0], -x[1]):  -x[1] means to take is_curr_matching=True over is_curr_matching=False
            pair[i, j] = max(pair[i, j], tmp)

    return back_trace(pair, len(sequence))


def back_trace(pair, length):
    letters = ['.'] * length
    count = pair[(0, length - 1)].count
    _back(0, length - 1, pair, letters)
    return count, "".join(letters)


def _back(left, right, pair, letters):
    if left < right:
        count, is_curr_matching, pre = pair[(left, right)]
        if is_curr_matching:
            letters[left], letters[right] = '(', ')'
            _back(left + 1, right - 1, pair, letters)
        elif count > 0:
            _back(left, pre, pair, letters)
            _back(pre + 1, right, pair, letters)


def isPair(a, b):
    """
    check if a, b is a pair of AU, GC or UG
    """
    pairs = {}
    pairs["A"] = set(["U"])
    pairs["U"] = set(["A", "G"])
    pairs["G"] = set(["C", "U"])
    pairs["C"] = set(["G"])
    return b in pairs[a] or a in pairs [b]


def total(sequence):
    """
    Total number of all possible structures
    GCAC G
    0123 4
    """
    pair = defaultdict(int)
    for i in xrange(len(sequence)):
        pair[i, i] = 1
        pair[i, i - 1] = 1

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            j = i + size - 1
            pair[i, j] += pair[i, j - 1]
            for k in xrange(i, j):
                if isPair(sequence[k], sequence[j]):
                    pair[i, j] += pair[i, k - 1] * pair[k + 1, j - 1]

    return pair[0, len(sequence) - 1]


def kbest(sequence, k):
    pair = defaultdict(list)
    rec = namedtuple("rec", "count splt lft_idx rgt_idx rst")
    for i in xrange(len(sequence) + 1):
        pair[i, i].append((0, '.'))
        pair[i, i - 1].append((0, ''))

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            klist, j = [], i + size - 1

            # initialize the candidates in the heap
            cnt, pre = pair[i, j - 1][0]
            klist.append((-cnt, float("inf"), 0, 0, pre + '.'))
            for t in xrange(i, j):
                if isPair(sequence[t], sequence[j]):
                    lcnt, left = pair[i, t - 1][0]
                    rcnt, right = pair[t + 1, j - 1][0]
                    klist.append(rec(count=-lcnt - rcnt - 1,
                        splt=t, lft_idx=0, rgt_idx=0, rst=left + '(' + right + ')'))
            heapq.heapify(klist)

            # Get k best options
            while len(pair[i, j]) < k and len(klist) > 0:
                cnt, t, lidx, ridx, candi = heapq.heappop(klist)
                pair[i, j].append((-cnt, candi))
                if t == float("inf"):
                    if lidx + 1 < len(pair[i, j - 1]):
                        ccnt, ppre = pair[i, j - 1][lidx + 1]
                        heapq.heappush(klist, (-ccnt, float("inf"), lidx + 1, 0, ppre + '.'))
                else:
                    lcnt, left = pair[i, t - 1][lidx]
                    rcnt, right = pair[t + 1, j - 1][ridx]
                    if lidx + 1 < len(pair[i, t - 1]):
                        llcnt, lleft = pair[i, t - 1][lidx + 1]
                        heapq.heappush(klist, (-llcnt - rcnt - 1,
                                               t, lidx + 1, ridx, lleft + '(' + right + ')'))

                    if ridx + 1 < len(pair[t + 1, j - 1]):
                        rrcnt, rright = pair[t + 1, j - 1][ridx + 1]
                        heapq.heappush(klist, (-lcnt - rrcnt - 1,
                                               t, lidx, ridx + 1, left + '(' + rright + ')'))

    return pair[0, len(sequence) - 1]

if __name__ == '__main__':
    print best("ACAGU")
    print total("ACAGU")
    print kbest("ACAGU", 10)
    print "-----------------------"
    print best("UUUGGCACUA")
    print total("UUUGGCACUA")
    print kbest("UUUGGCACUA", 100)
    print "-----------------------"
    print best("GAUGCCGUGUAGUCCAAAGACUUC")
    print total("GAUGCCGUGUAGUCCAAAGACUUC")
    print kbest("GAUGCCGUGUAGUCCAAAGACUUC", 100)
    print "-----------------------"
    print best("AGGCAUCAAACCCUGCAUGGGAGCG")
    print total("AGGCAUCAAACCCUGCAUGGGAGCG")
    print kbest("AGGCAUCAAACCCUGCAGGCAUCAAACCCUGCAGCCUGCAGGCAUCAAACCCUGCAGGCAUCAAACCCUGAUGGGAGCG", 100)
