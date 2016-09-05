# -*- coding: utf-8 -*-
# 31. Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            pass
        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break
        # print partition
        if partition == -1:
            # 54321 -> 12345
            nums.reverse()
            return
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    # 12354 -> 12453 (-> 12435)
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        nums[partition + 1: len(nums)] = nums[partition + 1: len(nums)][::-1]
        print nums

Solution().nextPermutation([1, 2])
Solution().nextPermutation([1, 2, 3, 4])
Solution().nextPermutation([1, 3, 2, 4])
Solution().nextPermutation([4, 3, 2, 1])