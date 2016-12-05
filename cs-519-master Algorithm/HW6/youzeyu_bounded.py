from operator import itemgetter
def best(W, lst):
    if lst == []:
        return 0,[]
    track={}
    def top_down(w, n, opt={(0,-1):0}):
        if w < 0 or n < 0:
            return 0
        if (w,n) in opt:
            return opt[(w,n)]
        newlst = [top_down(w-j*lst[n][0],n-1)+j*lst[n][1] if w >= j*lst[n][0] else 0 for j in xrange(lst[n][2]+1)]
        track[(w,n)],opt[(w,n)] = max(enumerate(newlst),key=itemgetter(1))
        return opt[(w,n)]
    return top_down(W,len(lst)-1), tracking(W,len(lst)-1, lst, track)

def tracking(w, n, lst, tracklst):
    if tracklst == {}:
        return []
    idxlst = [0]*len(lst)
    while w > 0 and n >= 0:
        idxlst[n] += tracklst[(w,n)]
        w -= tracklst[(w,n)]*lst[n][0]
        n -= 1
    return idxlst

if __name__ == "__main__":
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))