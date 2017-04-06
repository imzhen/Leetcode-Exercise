#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element
#
# Easy (37.30%)
# Total Accepted:    184411
# Total Submissions: 487061
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array and a value, remove all instances of that value in place and
# return the new length.
#
#
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
#
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
#
# Your function should return length = 2, with the first two elements of nums
# being 2.
#
#
# Try two pointers.
# Did you use the property of "the order of elements can be changed"?
# What happens when the elements to remove are rare?
#
#


class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        pos = 0
        for value in nums:
            if value != val:
                nums[pos] = value
                pos += 1
        return pos
