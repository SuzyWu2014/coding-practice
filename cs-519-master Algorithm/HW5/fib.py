import time


def fib2(n, cache=None):
                if cache is None:
                    cache = {}
                if n in cache:
                    return cache[n]
                print "calculating", n
                cache[n] = 1 if n <= 2 else fib2(n-1, cache) + fib2(n-2, cache)
                return cache[n]


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for i in range(5, 35):
        time1 = time.time()
        fib(i)
        elaspse = time.time() - time1
        print("{} {}".format(i, elaspse))