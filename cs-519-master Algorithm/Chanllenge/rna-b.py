from collections import defaultdict, namedtuple
import heapq


def kbest(sequence, k):
    pair = defaultdict(list)
    for i in xrange(len(sequence)):
        pair[i, i] = [(0, '.')]
        pair[i, i - 1] = [(0, '.')]

    for size in xrange(2, len(sequence) + 1):
        for i in xrange(len(sequence) - size + 1):
            klist = []
            # i and j are paired
            if isPair(sequence[i], sequence[i + size - 1]):
                while len(pair[i + 1, i + size - 2]) > 0:
                    cnt, pre = heapq.heappop(pair[i + 1, i + size - 2])
                    if len(klist) < k:
                        heapq.heappush(klist, (cnt + 1, '(' + pre + ')'))
                    elif cnt >= klist[0][0]:
                        heapq.heappush(klist, (cnt + 1, '(' + pre + ')'))
                    else:
                        break

            # i and j are not paired
            while len(pair[i, i + size - 2]) > 0:
                cnt, pre = heapq.heappop(pair[i, i + size - 2])
                if len(klist) < k:
                    heapq.heappush(klist, (cnt, pre + '.'))
                elif cnt >= klist[0][0]:
                    heapq.heappush(klist, (cnt, pre + '.'))
                else:
                    break

            for t in xrange(i + 1, i + size - 1):
                if isPair(sequence[i + size - 1], sequence[t]):
                    lcnt, left = heapq.heappop(pair[i, t - 1])
                    rcnt, right = heapq.heappop(pair[t + 1, i + size - 2])
                    while len(pair[i, t - 1]) > 0 or len(pair[t + 1, i + size - 2]) > 0:
                        if lcnt + rcnt + 1 >= klist[0][0]:
                            heapq.heappush(klist, (lcnt + rcnt + 1, left + '(' + right + ')'))
                        if lcnt >= rcnt and len(pair[i, t - 1]) > 0:
                            lcnt, left = heapq.heappop(pair[i, t - 1])
                        elif lcnt < rcnt and len(pair[t + 1, i + size - 2]) > 0:
                            rcnt, right = heapq.heappop(pair[t + 1, i + size - 2])
                        else:
                            break

            return pair[0, len(sequence) - 1]




