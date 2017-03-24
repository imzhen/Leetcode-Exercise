#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.10%)
# Total Accepted:    183156
# Total Submissions: 867399
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
#
# Note: The solution set must not contain duplicate triplets.
#
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# [-1, 0, 1],
# [-1, -1, 2]
# ]
#
#


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            val = nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                temp = nums[lo] + nums[hi] + val
                if temp > 0:
                    hi -= 1
                elif temp < 0:
                    lo += 1
                else:
                    result.append([val, nums[lo], nums[hi]])
                    hi -= 1
                    lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
        return result
