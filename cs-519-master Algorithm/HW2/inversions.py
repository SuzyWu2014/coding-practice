def num_inversions(nums):
    sorted_nums, inversions = _num_inversions(nums)
    return inversions


def _num_inversions(nums):
    if nums is None or len(nums) <= 1:
        return nums, 0
    mid = len(nums) // 2
    left, l_count = _num_inversions(nums[:mid])
    right, r_count = _num_inversions(nums[mid:])
    merged, merge_count = _merge(left, right)
    return merged, l_count + r_count + merge_count


def _merge(left, right):
    if left == []:
        return right, 0
    if right == []:
        return left, 0
    if left[0] <= right[0]:
        sub_merge, sub_count = _merge(left[1:], right)
        return [left[0]] + sub_merge, sub_count
    else:
        sub_merge, sub_count = _merge(left, right[1:])
        return [right[0]] + sub_merge, sub_count + len(left)


def _merge2(left, right):
    count, l_index, r_index = 0, 0, 0
    merged = []
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            merged.append(left[l_index])
            l_index += 1
        else:
            merged.append(right[r_index])
            r_index += 1
            count += len(left) - l_index
    if l_index == len(left):
        return merged + right[r_index:], count
    else:
        return merged + left[l_index:], count
