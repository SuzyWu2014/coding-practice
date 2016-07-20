# 81. Search in Rotated Sorted Array II
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid]:
                low += 1
            elif nums[high] == nums[mid]:
                high -= 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

print Solution().search([1], 2)
print Solution().search([2, 1], 2)
print Solution().search([2, 1], 1)
print Solution().search([1, 3], 3)
print Solution().search([1, 3, 5], 1)
