#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water
#
# Medium (36.16%)
# Total Accepted:    115284
# Total Submissions: 318834
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height) - 1
        result = min(height[0], height[-1]) * (hi - lo)
        while lo < hi:
            area_curr = min(height[lo], height[hi]) * (hi - lo)
            result = max(area_curr, result)
            if height[lo] < height[hi]:
                lo += 1
            elif height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1
                hi -= 1
        return result
