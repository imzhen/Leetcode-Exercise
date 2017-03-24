#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses
#
# Medium (42.29%)
# Total Accepted:    134629
# Total Submissions: 313567
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# "((()))",
# "(()())",
# "(())()",
# "()(())",
# "()()()"
# ]
#
#


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left, right = 0, 0
        curr = []
        result = []
        self.generateParenthesisHelper(n, left, right, curr, result)
        return result

    def generateParenthesisHelper(self, n, left, right, curr, result):
        if left == n and right == n:
            result.append(''.join(curr))
            return
        if left < n:
            curr.append('(')
            self.generateParenthesisHelper(n, left + 1, right, curr, result)
            curr.pop()
        if right < left:
            curr.append(')')
            self.generateParenthesisHelper(n, left, right + 1, curr, result)
            curr.pop()
