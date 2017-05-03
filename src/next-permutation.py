#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation
#
# Medium (28.24%)
# Total Accepted:    102758
# Total Submissions: 360926
# Testcase Example:  '[1]'
#
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
#
# The replacement must be in-place, do not allocate extra memory.
#
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 &#8594; 1,3,2
# 3,2,1 &#8594; 1,2,3
# 1,1,5 &#8594; 1,5,1
#
#


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        curr = len(nums) - 2
        while curr >= 0 and nums[curr] >= nums[curr + 1]:
            curr -= 1
        if curr < 0:
            nums[:] = sorted(nums[:])
            return
        new_curr = curr + 1
        while new_curr < len(nums) and nums[new_curr] > nums[curr]:
            new_curr += 1
        nums[curr], nums[new_curr - 1] = nums[new_curr - 1], nums[curr]
        nums[(curr + 1):] = sorted(nums[(curr + 1):])
        return
