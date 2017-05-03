#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say
#
# Easy (32.87%)
# Total Accepted:    128749
# Total Submissions: 383122
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
#
#
# Given an integer n, generate the nth sequence.
#
#
#
# Note: The sequence of integers will be represented as a string.
#
#
#


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return ""
        curr = '1'
        while n > 1:
            slow, fast = 0, 0
            result = ""
            while fast < len(curr):
                if curr[fast] == curr[slow]:
                    fast += 1
                else:
                    result += "%s%s" % (fast - slow, curr[slow])
                    slow = fast
            result += "%s%s" % (fast - slow, curr[slow])
            curr = result
            n -= 1
        return curr
