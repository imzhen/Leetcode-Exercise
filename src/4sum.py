#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum
#
# Medium (25.87%)
# Total Accepted:    107128
# Total Submissions: 412246
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
#
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# [-1,  0, 0, 1],
# [-2, -1, 1, 2],
# [-2,  0, 0, 2]
# ]
#
#


class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        curr_stack = []
        result = []
        self.kSum(nums, target, 4, curr_stack, result)
        return result

    def kSum(self, nums, target, k, curr_stack, result):
        if k > 2:
            for i in range(len(nums) - k + 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                self.kSum(nums[(i + 1):], target - nums[i],
                          k - 1, curr_stack + [nums[i]], result)
        else:
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                temp = nums[lo] + nums[hi]
                if temp > target:
                    hi -= 1
                elif temp < target:
                    lo += 1
                else:
                    result.append(curr_stack + [nums[lo], nums[hi]])
                    hi -= 1
                    lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
        return
