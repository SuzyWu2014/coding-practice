from collections import defaultdict
from heapq import *
allowedpairs = ["AU", "UA", "CG", "GC", "UG", "GU"]

def best(seq):
    lenseq = len(seq)
    opt = defaultdict(lambda: defaultdict(int))
    shape = defaultdict(lambda: defaultdict(str))
    for l in xrange(lenseq+1):
        for i in xrange(lenseq):
            if i+l <= lenseq:
                j = i+l
                if l == 0:
                    continue
                if l == 1:
                    shape[i][j] = "."
                    continue
                if seq[i]+seq[j-1] in allowedpairs:
                    opt[i][j] = 1+opt[i+1][j-1]
                    shape[i][j] = "("+shape[i+1][j-1]+")"
                for k in xrange(i+1, j):
                    if opt[i][k]+opt[k][j] > opt[i][j]:
                        opt[i][j] = opt[i][k]+opt[k][j]
                        shape[i][j] = shape[i][k]+shape[k][j]
                if opt[i][j] == 0:
                    shape[i][j] = "."*(j-i)
    return opt[0][lenseq], shape[0][lenseq]

def total(seq):
    lenseq = len(seq)
    opt = defaultdict(lambda : defaultdict(int))
    pair = defaultdict(lambda : defaultdict(int)) ## num of structures that forms an outer pair
    for l in xrange(lenseq+1):
        for i in xrange(lenseq):
            if i+l <= lenseq:
                j = i+l
                if l <= 1:
                    opt[i][j] = 1
                    continue
                if seq[i]+seq[j-1] in allowedpairs:
                    pair[i][j] = opt[i+1][j-1]
                opt[i][j] += opt[i+1][j] ## first one is unpaired
                opt[i][j] += pair[i][j] ## first one forms a pair with last one
                for k in xrange(i+1, j):
                    opt[i][j] += pair[i][k] * opt[k][j] ## first one forms a pair with an element in the middle
    return opt[0][lenseq]

def nbest_max(a, b, m):
    if len(a) == 0 or len(b) == 0:
        return []
    mykey = lambda u,v: -u[0]-v[0]
    sa, sb = sorted(a, reverse=True), sorted(b, reverse=True)
    result, h, ifused = [], [], set()

    heappush(h, (mykey(sa[0],sb[0]), (0,0)))
    while len(result) < m and len(h) > 0:
        i,j = heappop(h)[1]
        result.append((sa[i],sb[j]))
        if i+1<len(a) and (i+1,j) not in ifused:
            heappush(h, (mykey(sa[i+1],sb[j]), (i+1,j)))
            ifused.add((i+1,j))
        if j+1<len(b) and (i,j+1) not in ifused:
            heappush(h, (mykey(sa[i],sb[j+1]), (i,j+1)))
            ifused.add((i,j+1))
    return result

cnt = 2
def kbest(seq, m):
    lenseq = len(seq)
    strcache = defaultdict(str)
    strcache[0] = ""
    strcache[1] = "."
    global cnt
    cnt = 2
    hopt = defaultdict(lambda: defaultdict(list))
    shopt = defaultdict(lambda : defaultdict(set))
    opt = defaultdict(lambda: defaultdict(list))
    pair = defaultdict(lambda: defaultdict(list))

    def getpair(i, j, kth, hopt=hopt, opt=opt, shopt=shopt, pair=pair, strcache=strcache):
        if seq[i]+seq[j-1] not in allowedpairs:
            return None
        global cnt
        l = j-i
        if kth < len(pair[i][j]):
            return pair[i][j][kth]
        if l <= 1:
            return None
        inner = getopt(i+1,j-1,kth)
        if inner is not None:
            strcache[cnt] = "("+strcache[inner[1]]+")"
            pair[i][j].append((inner[0]-1, cnt, ("i",kth)))
            cnt += 1
        if kth >= len(pair[i][j]):
            return None
        return pair[i][j][kth]

    def getopt(i, j, kth, hopt=hopt, opt=opt, shopt=shopt, pair=pair, strcache=strcache):
        global cnt
        l = j-i
        if kth < len(opt[i][j]):
            return opt[i][j][kth]
        if l <= 1:
            if kth == 0:
                opt[i][j].append((0, l, None))
                return opt[i][j][0]
            else:
                return None
        if kth == 0:
            if seq[i]+seq[j-1] in allowedpairs:
                p = getpair(i,j,0)
                if p is not None:
                    heappush(hopt[i][j], (p[0], p[1], ("i", 0)))
            right = getopt(i+1,j,0)
            if right is not None:
                strcache[cnt] = "."+strcache[right[1]]
                heappush(hopt[i][j], (right[0], cnt, ("r",0)))
                cnt += 1
            for k in xrange(i+1, j):
                left = getpair(i,k,0)
                if left is None:
                    continue
                right = getopt(k,j,0)
                if right is None:
                    continue
                strcache[cnt] = strcache[left[1]]+strcache[right[1]]
                heappush(hopt[i][j], (left[0]+right[0], cnt, ("c",k,0,0)))
                cnt += 1
                shopt[i][j].add((k,0,0))
        if len(hopt[i][j]) == 0:
            return None
        result = heappop(hopt[i][j])
        if m > kth+1 and result[2] is not None:
            backptr = result[2]
            if backptr[0] == "i":
                bkth = backptr[1]
                p = getpair(i,j,bkth+1)
                if p is not None:
                    heappush(hopt[i][j], (p[0], p[1], ("i",bkth+1)))
            elif backptr[0] == "r":
                bkth = backptr[1]
                right = getopt(i+1,j,bkth+1)
                if right is not None:
                    strcache[cnt] = "."+strcache[right[1]]
                    heappush(hopt[i][j], (right[0], cnt, ("r", bkth+1)))
                    cnt += 1
            elif backptr[0] == "c":
                _, k, bkth_left, bkth_right = backptr
                left0 = getpair(i,k,bkth_left)
                left1 = getpair(i,k,bkth_left+1)
                right0 = getopt(k,j,bkth_right)
                right1 = getopt(k,j,bkth_right+1)
                if left0 is not None:
                    if right1 is not None:
                        if (k,bkth_left,bkth_right+1) not in shopt[i][j]:
                            strcache[cnt] = strcache[left0[1]]+strcache[right1[1]]
                            heappush(hopt[i][j], (left0[0]+right1[0], cnt, ("c",k,bkth_left,bkth_right+1)))
                            cnt += 1
                            shopt[i][j].add((k,bkth_left,bkth_right+1))
                if left1 is not None:
                    if right0 is not None:
                        if (k,bkth_left+1,bkth_right) not in shopt[i][j]:
                            strcache[cnt] = strcache[left1[1]]+strcache[right0[1]]
                            heappush(hopt[i][j], (left1[0]+right0[0], cnt, ("c",k,bkth_left+1,bkth_right)))
                            cnt += 1
                            shopt[i][j].add((k,bkth_left+1,bkth_right))
                    if right1 is not None:
                        if (k,bkth_left+1,bkth_right+1) not in shopt[i][j]:
                            strcache[cnt] = strcache[left1[1]]+strcache[right1[1]]
                            heappush(hopt[i][j], (left1[0]+right1[0], cnt, ("c",k,bkth_left+1,bkth_right+1)))
                            cnt += 1
                            shopt[i][j].add((k,bkth_left+1,bkth_right+1))

        opt[i][j].append(result)
        return result

    for kth in xrange(m):
        result = getopt(0,lenseq, kth)
        if result is None:
            break
    return [(-v,strcache[s]) for v,s,_ in opt[0][lenseq]]

if __name__ == "__main__":

#     testcases = [
#         "ACAGU",
#         "UUCAGGA",
#         "GUUAGAGUCU",
#         "GCACG",
#         "AUAACCUUAUAGGGCUCUG",
#         "UUGGACUUGAGAAAAG",
#         "UCAAUGGGUAGUAAAU",
#         "UUUGGCACUUUCAGA",
#         "ACACACCUUGUCCGUGAA",
#         "GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG",
#         "CGCGAAUAAAAAGGCACUGUU",
#         "ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC",
#         "UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU",
#         "AUACGUCGGGGACAAGAAUUACGG",
#         "AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA",
#         "CGAGGUGGCACUGACCAAACACCACCGAAAC",
#         "CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU",
#         "CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU",
#         "AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU",
# ]

    testcases = [
        "AGGCAUCAAACCCUGCAUGGGAGCGAGGCAUCAAACCCUGCAUGGGAGCGAGGCAUCAAACCCUGCAUGGGAGCG",
    ]

    for testcase in testcases:
        testcase
        best(testcase)
        total(testcase)
        kbest(testcase, 100)
        #print "------"
