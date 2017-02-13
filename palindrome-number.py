#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number
#
# Easy (34.09%)
# Total Accepted:    182761
# Total Submissions: 536052
# Testcase Example:  '-2147483648'
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
#
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
#
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
#
# There is a more generic way of solving this problem.
#
#
#


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if not x or x < 0 or x % 10 == 0:
            return False
        rev = 0
        while x > rev:
            x, m = divmod(x, 10)
            rev = rev * 10 + m
        return rev == x or rev / 10 == x
