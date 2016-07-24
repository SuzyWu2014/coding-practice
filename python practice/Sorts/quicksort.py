# 快速排序

# partition
# 1 以第一个数为基准pivot，
# 2 先从左到右与pivot对比, 直至left > pivot时停止
# 3 从右到左与pivot对比，直至right < pivot 时停止
# 4 交换此时left 与 right 的值
# 5 重复步骤2 － 4， 直至left > right, 交换 right 与 left的值
# 6 最后交换此时left 与 pivot 的值
# 7 返回目前数组pivot的位置；

# 经过一轮交换， pivot 确定了他的位置，因为左边的值都比它小，而右边都比它大

# quicksort
# 以第一个数为基准，找到partitiion
# 将数组分成左右两边，进行quicksort


def findPartition(nums, left, right):
    pivot = nums[left]
    left += 1

    while left < right:
        while left < right and pivot <= nums[right]:
            right -= 1
        while left < right and pivot > nums[left]:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]

    nums[0], nums[left] = nums[left], nums[0]

    return left


def doQuicksort(nums, left, right):
    if left < right:
        partition = findPartition(nums, left, right)
        doQuicksort(nums, left, partition - 1)
        doQuicksort(nums, partition + 1, right)


def quicksort(nums):
    doQuicksort(nums, 0, len(nums) - 1)
    return nums

print(quicksort([9, 3]))
print(quicksort([9, 3, 4, 5, 6]))
