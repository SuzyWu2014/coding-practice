__author__ = "liang huang"

from heapq import heapify, heappop, heappush
from collections import defaultdict
allowed = set(['AU','UA','CG','GC','GU','UG'])

def best(s):

    def update(i, j, value, trace):
        if value > opt[i, j]:
            opt[i, j] = value
            back[i, j] = trace
    
    def solution(i, j):
        if i == j: # empty
            return ""
        elif i == j-1: # singleton
            return "."
        t = back[i, j]
        if t == -1: # pair
            return "(%s)" % solution(i+1, j-1) 
        return "%s%s" % (solution(i, t), solution(t, j)) # split

    n = len(s)
    opt = defaultdict(lambda : -1)
    back = {}
    for i in xrange(n):
        opt[i, i+1] = 0
        opt[i, i] = 0

    for span in xrange(2, n+1): # span length: 2..n
        for i in xrange(n-span+1): # left boundary: 0..(n-span)
            j = i+span # right boundary
            
            if s[i]+s[j-1] in allowed: # pair (___)
                update(i, j, opt[i+1, j-1] + 1, -1)
            for k in xrange(i+1, j): # split point: i+1..j-1
                update(i, j, opt[i, k] + opt[k, j], k)
            
    return opt[0, n], solution(0, n)

def total(s):

    ''' tot[i,j] -- total; pair[i,j] -- subset of total with i--(j-1): (xxxx)'''

    n = len(s)
    tot = defaultdict(int)

    for i in xrange(n+1): # NB
        tot[i, i+1] = 1 # singleton .
        tot[i, i] = 1 # empty

    for span in xrange(2, n+1): # span length: 2..n
        for i in xrange(n-span+1): # left boundary: 0..(n-span)
            j = i+span # right boundary
            
            tot[i, j] += tot[i+1, j] # case 1: i unpaired 

            for k in xrange(i+1, j+1): # split point: i+1..j-1
                if s[i]+s[k-1] in allowed: # pair (___)                    
                    tot[i, j] += tot[i+1, k-1] * tot[k, j] # case 3: i paired with k-1 (k<j)

    return tot[0, n]

def kbest(s, k):

    def tryadd(split, index1, index2):
        if index1 < len(opt[i, split]) and index2 < len(opt[split, j]) \
           and not (split, index1, index2) in used:
            used.add((split, index1, index2))
            heappush(heap, 
                     (-opt[i, split][index1][0]-opt[split, j][index2][0], split, index1, index2))

    def tryadd1(index):
        if index < len(opt[i+1, j-1]):
            heappush(heap, (-opt[i+1, j-1][index][0]-1, index)) # min-heap

    def add_candidate(value, struct):
        if struct not in uniq:
            uniq.add(struct)
            opt[i, j].append((-value, struct)) # value was negative in heap

    n = len(s)
    opt = defaultdict(list) # list of (value, structure) pairs
    for i in xrange(n):
        opt[i, i+1] = [(0, '.')] # singleton
        opt[i, i] = [(0, '')] # empty

    for span in xrange(2, n+1): # span length: 2..n
        for i in xrange(n-span+1): # left boundary: 0..(n-span)
            j = i+span # right boundary

            heap = []            
            used = set()

            if s[i]+s[j-1] in allowed: # pair (___)
                #heap.append((-opt[i+1, j-1][0][0]-1, 0)) # min-heap
                tryadd1(0)
            for m in xrange(i+1, j): # split point: i+1..j-1
                tryadd(m, 0, 0)

            heapify(heap)
            uniq = set() # uniq k-best structures

            while heap != [] and len(opt[i, j]) < k:
                item = heappop(heap)
                if len(item) == 2: # pair
                    value, index = item
                    add_candidate(value, "(%s)" % opt[i+1,j-1][index][1]) # check duplicates
                    tryadd1(index+1)
                else: # split
                    value, split, index1, index2 = item
                    add_candidate(value, "%s%s" % (opt[i, split][index1][1],
                                                   opt[split, j][index2][1]))
                    tryadd(split, index1+1, index2)
                    tryadd(split, index1, index2+1)

    return opt[0,n]#, solution(0, n)

print best("ACAGU")
print total("ACAGU")
print kbest("ACAGU", 10)
