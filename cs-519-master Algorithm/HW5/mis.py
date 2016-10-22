def max_wis2(nums):
    """
    Maximum Weighted Independent Set
    input:  a list of numbers (could be negative)
    output: a pair of the max sum and the list of numbers chosen

    dp[i]: max of
                  - contains item i + dp[i-2]
                  - not contain item i, and dp[i-1]
    """
    if nums is None or nums == []:
        return (0, [])
    dp = []
    if len(nums) >= 1:
        dp.append((nums[0], [nums[0]]) if nums[0] > 0 else (0, []))
    if len(nums) >= 2:
        dp.append(max((nums[1], [nums[1]]), dp[0]))
    for i in xrange(2, len(nums)):
        dp.append(max((nums[i], [nums[i]]),
                        (nums[i] + dp[i - 2][0], dp[i - 2][1] + [nums[i]]),
                        dp[i - 1]))
    return dp[len(nums) - 1]


def memorize(func):
    d = dict()

    def wrapper(*args):
        if args in d:
            return d[args]
        else:
            result = func(*args)
            d[args] = result
            return result
    return wrapper

def _max_wis(size, nums, item_dict=None):
    """
    item_dict[curr_item] = (max_sum, pre_item, with_current_item )
    """
    if item_dict is None or len(item_dict) == 0:
        item_dict = dict()
        item_dict[-1] = (0, -1, False)
        item_dict[-2] = (0, -1, False)
    elif size in item_dict:
        return item_dict

    item_dict[size] = max((_max_wis(size - 1, nums, item_dict)[size - 1][0], size - 1, False),
        (nums[size] + _max_wis(size - 2, nums, item_dict)[size - 2][0], size - 2, True))
    return item_dict

def max_wis(nums):
    if nums is None or nums == []:
        return (0, [])
    item_dict = _max_wis(len(nums) - 1, nums)
    max_sum, _, _ = item_dict[len(nums) - 1]
    items = []
    curr = len(nums) - 1
    while 1:
        _, pre, if_curr = item_dict[curr]
        if if_curr:
            items.append(nums[curr])
        if pre == -1:
            break
        curr = pre
    return (max_sum, list(reversed(items)))

if __name__ == '__main__':
    print(max_wis([]))
    print(max_wis([-1]))
    print(max_wis([1,2]))
    print(max_wis([1,-2]))

    # print(max_wis2([]))
    # print(max_wis2([-1]))
    # print(max_wis2([1,2]))
    # print(max_wis2([1,-2]))

    print(max_wis2([7,8,5]))
    print(max_wis([7,8,5]))
    print(max_wis2([-1,8,10]))
    print(max_wis([-1,8,10]))
    print(max_wis2([1,8,2,10,6, -3, -4, -5, 10]))
    print(max_wis([1,8,2,10,6, -3, -4, -5, 10]))
