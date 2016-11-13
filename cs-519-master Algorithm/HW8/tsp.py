import collections
import itertools
import math


def tsp(cities):
    """
    @cities: (index, x, y)
    """
    size = len(cities)
    route = collections.namedtuple("route", "distance pre_city")
    cache = collections.defaultdict(lambda: route(float("inf"), -1))
    # From city 0 to city i
    for i, sub in enumerate(city_sets(size, 1)):
        cache[(i + 1, sub)] = route(distance(cities, 0, i + 1), 0)

    # From city 0 to city k via a set of cities(i..m..k)
    for cnt in xrange(2, size):
        for subset in city_sets(size, cnt):
            for city in subset:
                pre_set = tuple(i for i in subset if i != city)
                tmp = min([route(cache[(m, pre_set)].distance + distance(cities, m, city), pre_city=m) for m in pre_set])
                cache[(city, subset)] = min(cache[(city, subset)], tmp)

    # Back to city 0
    cache[(0, tuple(xrange(0, size)))] = min([route(cache[(i, tuple(xrange(1, size)))].distance + distance(cities, i, 0), pre_city=i) for i in xrange(1, size)])

    return cache[(0, tuple(xrange(0, size)))].distance, back_trace(size, cache)


def back_trace(size, cache):
    res = [0]
    city_set = set(xrange(0, size))
    curr = 0
    while city_set:
        _, pre = cache[(curr, tuple(sorted(city_set)))]
        res.append(pre)
        city_set.remove(curr)
        curr = pre
    return res


def city_sets(total_city, num_city):
    return itertools.combinations(xrange(1, total_city), num_city)


def distance(cities, src, dest):
    a, b = cities[src], cities[dest]
    return math.sqrt(pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))

# def city_sets2(total_city, num_city):
#     tmp = itertools.combinations(xrange(1, total_city), num_city)
#     res = []
#     for subset in tmp:
#         tmp = 0
#         for i in subset:
#             tmp += 1 << i
#         res.append(tmp)
#     return res

if __name__ == '__main__':
    print(tsp([(0, 0, 0), (1, 1, 1), (2, 1, 0), (3, 0, 1)]))
    print(tsp([(0, 1, 0), (1, 0, 1), (2, 0, 0), (3, 1, 1)]))
    print(tsp([(0, 0, 0), (1, 1, 1), (2, 1, 0), (3, 0, 1), (4, 0.5, 1.5)]))
    print(tsp([(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 2, 2), (5, 2, 3), (6, 2, 3), (7, 1, 2)]))
    print(tsp([(0, 1, 1), (1, 2, 1), (2, 2, 2), (3, 2, 3), (4, 3, 1), (5, 4, 1), (6, 1, 2), (7, 2, 3)]))
