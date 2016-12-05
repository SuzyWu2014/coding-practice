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
        if right == len(nums) or (left >= 0 and abs(nums[left] - val) <= abs(nums[right] - val)):
            left -= 1
        else:
            right += 1
    return nums[left + 1:right]


if __name__ == "__main__":
    print find([1, 1, 1, 1, 1], 1, 0)
    print find([1, 1, 1, 1, 1], 1, 5)
    print find([1, 1, 1, 10, 10, 10], 5, 1)
    print find([1, 1, 1, 10, 10, 10], 3, 4)
    print find([1, 1, 1, 10, 10, 10, 10], 10, 4)
