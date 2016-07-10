import collections
# 217. Contains Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

# Solution 3: acceptable
# return len(nums) != len(set(nums))

# Solution 2: acceptable
#
# if len(nums) <= 1:
# 	return False
# else:
# 	nums = sorted(nums)
# 	ifDup = False
# 	for i in range(len(nums) - 1):
# 		if nums[i] == nums[i + 1]:
# 			return True
# 	return False

# Solution 1: Least efficient
#
# if len(nums) == 0:
# 	return False
# else:
# 	return nums[0] in nums[1:] or constainsDuplicate(nums[1:])


def constainsDuplicate(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	numSet = set()
	for num in nums:
		if num in numSet:
			return True
		numSet.add(num)
	return False
