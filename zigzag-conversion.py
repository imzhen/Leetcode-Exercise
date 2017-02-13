#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion
#
# Medium (26.07%)
# Total Accepted:    135535
# Total Submissions: 519691
# Testcase Example:  '""\n1'
#
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
#


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s
        result = [''] * numRows
        curr = 0
        down_flag = True
        for val in s:
            result[curr] += val
            if down_flag:
                if curr + 1 == numRows:
                    curr -= 1
                    down_flag = False
                else:
                    curr += 1
            else:
                if curr == 0:
                    curr += 1
                    down_flag = True
                else:
                    curr -= 1
        return ''.join(result)
