import heapq


def ksmallest(k, nums):
    """
    Find the k smallest numbers in a data stream of length n (k<<n),
    using only O(k) space (the stream itself might be too big to fit in memory).
    """
    if nums is None:
        return
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        elif -heap[0] > num:
            # heapq.heappushpop(heap, -num)
            heapq.heapreplace(heapq, -num)
    return sorted([-i for i in heap])
    # return sorted([-heapq.heappop(heap) for i in xrange(k)])


if __name__ == "__main__":
    print ksmallest(4, [3,6,5])
    print ksmallest(4, [1,3,4,5])
    print ksmallest(4, [1,1,2,1,-2,-1,-1,1,1,1])
    print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
    print ksmallest(3, xrange(1000000, 0, -1))
