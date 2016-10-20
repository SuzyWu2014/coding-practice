def max_wis(nums):
    """
    Maximum Weighted Independent Set
    input:  a list of numbers (could be negative)
    output: a pair of the max sum and the list of numbers chosen

    dp[i]: max of - only contains item i
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


if __name__ == '__main__':
    print(max_wis([]))
    print(max_wis([-1]))
    print(max_wis([1,2]))
    print(max_wis([1,-2]))
    print(max_wis([7,8,5]))
    print(max_wis([-1,8,10]))
    print(max_wis([1,8,2,10,6, -3, -4, -5, 10]))
