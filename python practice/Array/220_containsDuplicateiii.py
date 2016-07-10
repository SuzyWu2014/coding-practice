import collections
# 220. Contains Duplicate III
# Given an array of integers, find out whether there are two distinct indices i and j in the array
# such that the difference between nums[i] and nums[j] is at most t and
#           the difference between i and j is at most k.

"""
We have:  	|nums[i] - nums[j]| <= t
then: 	  	|nums[i]/t - nums[j]/t| <= 1
therefore: 	|floor(nums[i]/t) - floor(nums[j]/t)| <= 1
Finally:	floor(nums[j]/t) in {floor(nums[i]/t) -1, floor(nums[i]/t), floor(nums[i]/t)+1}
"""


def containsNearbyAlmostDuplicate(self, nums, k, t):
	"""
	:type nums: List[int]
	:type k: int
	:type t: int
	:rtype: bool
	"""
	if k < 1 or t < 0:
		return False
	numDict = collections.OrderedDict()
	for i in range(len(nums)):
		key = nums[i] / max(1, t)
		for m in {key, key - 1, key + 1}:
			if m in numDict and abs(nums[i] - numDict[m]) <= t:
				return True
		numDict[key] = nums[i]
		if i >= k:
			numDict.popitem(last=False)
	return False
