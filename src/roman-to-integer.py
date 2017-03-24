#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer
#
# Easy (43.97%)
# Total Accepted:    129541
# Total Submissions: 294529
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = ["M", "CM", "D", "CD", "C", "XC",
                   "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = 0
        for i in range(len(symbols)):
            while s.startswith(symbols[i]):
                result += nums[i]
                s = s[len(symbols[i]):]
        return result
