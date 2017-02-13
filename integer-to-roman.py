#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman
#
# Medium (43.14%)
# Total Accepted:    93132
# Total Submissions: 215863
# Testcase Example:  '1'
#
# Given an integer, convert it to a roman numeral.
#
#
# Input is guaranteed to be within the range from 1 to 3999.
#


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        symbols = ["M", "CM", "D", "CD", "C", "XC",
                   "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(symbols)):
            val, mod = divmod(num, nums[i])
            if val > 0:
                result += symbols[i] * val
            num = mod
        return result
