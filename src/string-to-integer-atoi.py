#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi
#
# Medium (13.84%)
# Total Accepted:    150054
# Total Submissions: 1084073
# Testcase Example:  '""'
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.
#
#
# Notes:
# It is intended for this problem to be specified vaguely (ie, no given input
# specs). You are responsible to gather all the input requirements up front.
#
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button  to reset your code definition.
#
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
#
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned. If the
# correct value is out of the range of representable values, INT_MAX
# (2147483647) or INT_MIN (-2147483648) is returned.
#
#
#


class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)
        str_stripped = str.strip()
        if not str_stripped:
            return 0
        if re.findall(r'^[0-9\-\+]', str_stripped):
            if str_stripped[0] in '+-':
                if str_stripped[1:]:
                    if re.findall(r'[0-9]', str_stripped[1]):
                        result = int(str_stripped[1])
                        for i in str_stripped[2:]:
                            if re.findall(r'[0-9]', i):
                                result = result * 10 + int(i)
                            else:
                                break
                        if str_stripped[0] == '-':
                            result = result * -1
                        if result < INT_MIN:
                            return INT_MIN
                        elif result > INT_MAX:
                            return INT_MAX
                        else:
                            return result
            else:
                result = int(str_stripped[0])
                for i in str_stripped[1:]:
                    if re.findall(r'[0-9]', i):
                        result = result * 10 + int(i)
                    else:
                        break
                if result > INT_MAX:
                    return INT_MAX
                else:
                    return result
        return 0
