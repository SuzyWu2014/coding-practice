# -*- coding: utf-8 -*-
# 堆排序 http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/

# 第一阶段：
# 构造最大堆
# heap 是一个 binary tree； 父节点大于等于子节点
# 叶子节点是leftmost

# 第二阶段：
# 堆排序
# 由于堆是由数组模拟的，得到大根堆以后，数组内部并不是有序的
# 思路：
#   移除根节点，并做最大堆调整
# 调整步骤：
#   1. heap[0] 与 heap[n-1] 交换，对heap[0..n-2] 做最大堆调整 => 最大值位置确认， heap[n]
#   2. heap[0] 与 heap[n-2] 交换，对heap[0..n-3] 做最大堆调整
#   3. 直至 heap[0] 与 heap[1] 交换，则排序结束

# 对于based on array 的heap 来说：
# 元素n的节点index为 2n+1 与 2n+2

# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点


def maxHeapify(nums, start, end):
    # start为当前需要调整最大堆的位置，end为调整边界
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            return
        if child + 1 <= end and nums[child] < nums[child + 1]:
            child += 1
        if nums[root] < nums[child]:
            nums[root], nums[child] = nums[child], nums[root]
            root = child
        else:
            return


def heapsort(nums):
    # convert nums to heap
    length = len(nums)
    least_parent = length / 2 - 1
    for start in range(least_parent, -1, -1):
        maxHeapify(nums, start, length - 1)
    # heapsort
    for end in range(length - 1, 0, -1):
        nums[end], nums[0] = nums[0], nums[end]
        maxHeapify(nums, 0, end - 1)
    return nums

print heapsort([3, 2, 1, 5, 6, 7, 4])
