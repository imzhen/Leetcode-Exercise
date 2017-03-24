#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest
#
# Medium (30.65%)
# Total Accepted:    116400
# Total Submissions: 379420
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
#
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        threshold = sys.maxint
        result = None
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            val = nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                temp = val + nums[lo] + nums[hi]
                if abs(temp - target) < threshold:
                    result = temp
                    threshold = abs(temp - target)
                if temp < target:
                    lo += 1
                elif temp > target:
                    hi -= 1
                else:
                    return target
        return result
