#CS519 -- Bounded Knapsack
#Name: Chunyang Zhang
#ID:   932-224-548

def best(W, A):
    cache, n = {(0, -1): (0, -1, 0)}, len(A)-1

    def opt(x, i, cache):
        if (x, i) in cache:
            return cache[(x, i)]
        if x == 0 or i == -1:
            return cache[(0, -1)]
        w,v,c = A[n-i]
        cache[(x,i)] = max((opt(x-w*j, i-1, cache)[0]+v*j, j) if x >= w*j else cache[(0,-1)] for j in range(c+1))
        return cache[(x, i)]

    def back(x, i):
        solution = [0]*(n+1)
        while x > 0 and i != -1 and cache[(x,i)][0] != 0:
            solution[n-i] = cache[(x,i)][1]
            x -= A[n-i][0] * cache[(x,i)][1]
            i -= 1
        return solution

    return opt(W, n, cache)[0], back(W, n)


if __name__ == "__main__":
    print best(3, [(2, 4, 2), (3, 5, 3)])
    print best(3, [(1, 5, 2), (1, 5, 3)])
    print best(3, [(1, 5, 1), (1, 5, 3)])
    print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
    print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
    print best(3, [(2, 3, 1), (1, 2, 1), (3, 4, 1)])

