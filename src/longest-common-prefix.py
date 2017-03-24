#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix
#
# Easy (30.72%)
# Total Accepted:    150417
# Total Submissions: 489467
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
#


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        counter = -1
        for i in range(len(strs[0])):
            for s in strs:
                if i > len(s) or not s.startswith(strs[0][:(i + 1)]):
                    return strs[0][:(counter + 1)]
                    break
            counter += 1
        return strs[0][:(counter + 1)]
