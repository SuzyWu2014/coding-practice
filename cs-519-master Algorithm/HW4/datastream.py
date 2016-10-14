import heapq


def ksmallest(k, nums):
    """
    Find the k smallest numbers in a data stream of length n (k<<n),
    using only O(k) space (the stream itself might be too big to fit in memory).
    """
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        elif -heap[0] > num:
            heapq.heappushpop(heap, -num)
    return sorted([-heapq.heappop(heap) for i in xrange(k)])


print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
print ksmallest(3, xrange(1000000, 0, -1))