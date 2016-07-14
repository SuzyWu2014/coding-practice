# 216. Combination Sum III
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        rst = []

        def find_sum(count, sub_sum, nums, start):
            if count > k or sub_sum > n:
                return
            if sub_sum == n and count == k:
                rst.append(nums)
                return
            for i in range(start + 1, 10):
                find_sum(count + 1, sub_sum + i, nums + [i], i)
        find_sum(0, 0, [], 0)
        return rst

print Solution().combinationSum3(3, 9)
