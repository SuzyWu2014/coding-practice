import collections
# 219. Contains Duplicate II
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.


def containsNearbyDuplicate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	numDict = dict()
	for i in range(len(nums)):
		numIndex = numDict.get(nums[i])
		if numIndex >= 0 and (i - numIndex) <= k:
			return True
		numDict[nums[i]] = i
	return False

# Solution 2: deque - Least efficient
# numDeque = deque()
# for num in nums:
# 	if num in numDeque:
# 		return True
# 	numDeque.append(num)
# 	if numDeque.count(k + 1):
# 		numDeque.popleft()

# Solution 1: Least efficient
# for i in range(len(nums) - k):
# 	if(constainsDuplicate(nums[i:i + k])):
# 		return True
# return False

print(containsNearbyDuplicate([-1, -1], 1))
