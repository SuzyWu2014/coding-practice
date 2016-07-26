# 300. Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        DP
        """
        if nums == []:
            return 0
        tb = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            tb[i][i] = 1
        for i in range(len(nums)):
            t = i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[t]:
                    tb[i][j] = tb[i][j - 1] + 1
                    t += 1
                else:
                    tb[i][j] = tb[i][j - 1]
                # print tb
        return max([row[len(nums) - 1] for row in tb])


print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
