# Use a long list of random numbers to show the difference in time. What about sorted or reversely-sorted numbers?

# 0. There are two methods for building a heap from an unsorted array:
#    (1) insert each element into the heap  --- O(nlogn)
#    (2) heapify (top-down)                 --- O(n)

import heapq
import time
import random


def heap_slow(nums):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
    return heap

def heap_fast(nums):
    heapq.heapify(nums)
    return nums


if __name__ == '__main__':
    print("heap_push\t\t\theapipy")
    for n in [10000, 100000, 1000000]:
        # nums1 = range(n)
        # nums2 = range(n, -1, -1)
        nums3 = [random.randint(0, n) for r in xrange(n)]
        for nums in [ nums3]:
            time1 = time.time()
            heap = heap_slow(nums)
            time_slow = time.time() - time1

            time1 = time.time()
            nums = heap_fast(nums)
            time_fast = time.time() - time1
            print time_slow, "\t\t\t", time_fast
