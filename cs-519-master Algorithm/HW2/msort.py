def mergesort(nums):
    if nums is None or len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    if left == []:
        return right
    if right == []:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def merge2(left, right):
    rst = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            rst.append(left[l])
            l += 1
        else:
            rst.append(right[r])
            r += 1
    if l == len(left):
        return rst + right[r:]
    else:
        return rst + left[l:]
