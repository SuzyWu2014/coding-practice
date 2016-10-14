# 167. Two Sum II - Input array is sorted
# Given an array of integers that is already sorted in ascending order, \
# find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while 1:
            mid = (left + right) // 2
            if numbers[left] + numbers[right] == target:
                return left + 1, right + 1
            if numbers[left] + numbers[mid] >= target:
                right = mid
            elif numbers[mid] + numbers[right] <= target:
                left = mid
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

print Solution().twoSum([1,2,3,4,4,9,56,90], 8)
print Solution().twoSum([0,0,3,4], 0)
print Solution().twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542)
