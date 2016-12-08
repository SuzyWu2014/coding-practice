import heapq


def kmergesort(nums, k):
    if nums is None or len(nums) <= 1:
        return nums
    klist = [[] for i in xrange(k)]
    size = len(nums) // k + 1
    for i, num in enumerate(nums):
        klist[i // size].append(num)
    klist = map(lambda x: kmergesort(x, k), klist)
    return merge(klist)


def merge(nums_list):
    return list(heapq.merge(*nums_list))

def merge2(nums_list):
    heap = [(nums[0], list_idx, 0 ) for list_idx, nums in enumerate(nums_list) if len(nums) > 0]
    heapq.heapify(heap)
    rst = []
    while len(heap) > 0:
        num, list_idx, item_idx = heapq.heappop(heap)
        rst.append(num)
        if item_idx + 1 < len(nums_list[list_idx]):
            heapq.heappush(heap, (nums_list[list_idx][item_idx + 1], list_idx, item_idx + 1))
    return rst


if __name__ == "__main__":
    print kmergesort([4,1,5,2,6,3,7,0], 3)
    print kmergesort([4,13,7,0], 8)
