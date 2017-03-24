#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses
#
# Easy (32.41%)
# Total Accepted:    182739
# Total Submissions: 558713
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
#
#


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in chars:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if chars[stack.pop()] != char:
                        return False
        if stack:
            return False
        return True
