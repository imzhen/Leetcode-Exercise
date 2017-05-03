#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# Medium (32.07%)
# Total Accepted:    158239
# Total Submissions: 492792
# Testcase Example:  '[]\n5'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if target == nums[mid]:
                return mid
            if nums[lo] <= nums[mid]:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        if nums[lo] == target:
            return lo
        else:
            return -1
