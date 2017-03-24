#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
#
# Medium (32.79%)
# Total Accepted:    133156
# Total Submissions: 401546
# Testcase Example:  '""'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
#
#
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
#
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#


class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = ['']
        for i in digits:
            result = [x + y for x in result for y in kvmaps[i]]
        return result
