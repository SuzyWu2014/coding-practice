def find(nums):
    """
    For a given array A of n *distinct* numbers,
    find all triples (x,y,z)
   s.t. x + y = z.
    """
    nums = sorted(nums)
    rst = []
    for i in range(len(nums)):
        findSum(nums, i, rst)
    return rst


def findSum(nums, target, rst):
    """
    find x + y = nums[target]
    """
    i = 1 if target == 0 else 0
    j = len(nums) - 2 if target == len(nums) - 1 else len(nums) - 1
    while i < j:
        if i == target or nums[i] + nums[j] < nums[target]:
            i += 1
        elif j == target or nums[i] + nums[j] > nums[target]:
            j -= 1
        elif nums[i] + nums[j] == nums[target]:
            rst.append((nums[i], nums[j], nums[target]))
            i += 1
            j -= 1
