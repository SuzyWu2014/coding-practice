import random


def find(nums, val, k):
    """
    find the k numbers in nums that are closest (in value) to x.
    """
    if nums is None or k < 0 or len(nums) < k:
        return
    diff = map(lambda x: abs(x - val), nums)
    kth_diff = quickselect(diff, k)
    less_kth = [i for i, num in enumerate(nums) if abs(num - val) < kth_diff ]
    equal_kth = [i for i, num in enumerate(nums) if abs(num - val) == kth_diff ]
    closest_k = merge(less_kth, equal_kth[:(k - len(less_kth))])
    return [nums[index] for index in closest_k]

def merge(left, right):
    rst = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if i == len(left):
            rst += right[j:]
            break
        elif j == len(right):
            rst += left[i:]
            break
        elif left[i] < right[j]:
            rst.append(left[i])
            i += 1
        else:
            rst.append(right[j])
            j += 1
    return rst


def find2(nums, val, k):
    """
    find the k numbers in nums that are closest (in value) to x.
    """
    if nums is None or k < 0 or len(nums) < k:
        return
    diff = map(lambda x: abs(x - val), nums)
    kth_diff = quickselect(diff, k)
    closest_k = [num for num in nums if abs(num - val) <= kth_diff]
    if len(closest_k) > k:
        count = len(closest_k) - k
        index = len(closest_k) - 1
        while count > 0:
            if abs(closest_k[index] - val) == kth_diff:
                closest_k.pop(index)
                count -= 1
            index -= 1
    return closest_k


def quickselect(nums, k):
    if nums is None or k <= 0 or len(nums) < k:
        return
    pivot = random.choice(nums)
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    if k <= len(left):
        return quickselect(left, k)
    elif k > len(nums) - len(right):
        return quickselect(right, k - (len(nums) - len(right)))
    else:
        return pivot
