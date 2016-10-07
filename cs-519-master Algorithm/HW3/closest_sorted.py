import bisect


def find(nums, val, k):
    """
    find the k numbers in sorted list that are closest (in value) to x.
    """
    if nums is None or k < 0 or len(nums) < k:
        return
    right = bisect.bisect_left(nums, val)
    left = right - 1
    while right - left - 1 < k:
        if right == len(nums) or abs(nums[left] - val) <= abs(nums[right] - val):
            left -= 1
        else:
            right += 1
    return nums[left + 1:right]


print find([1,2,3,4,4,7], 5.2, 2)
print find([1,2,3,4,4,7], 6.5, 3)
print find([1,2,3,4,4,6,6], 5, 3)
print find([1,2,3,4,4,5,6], 4, 5)
print find([1,1,2,3,4,4,5,6], 1, 5)


