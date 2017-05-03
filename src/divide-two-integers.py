#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers
#
# Medium (15.95%)
# Total Accepted:    96016
# Total Submissions: 601498
# Testcase Example:  '0\n1'
#
#
# Divide two integers without using multiplication, division and mod
# operator.
#
#
# If it is overflow, return MAX_INT.
#
#


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            if dividend >= 0:
                return 2 ** 31 - 1
            else:
                return - 2 ** 31
        if dividend == 0:
            return 0
        if dividend == - 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            signal = False
        else:
            signal = True

        result = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            shift = 0
            while a >= b << shift:
                shift += 1
            a -= b << (shift - 1)
            result += 1 << (shift - 1)
        if signal:
            return result
        else:
            return -result
