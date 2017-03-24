#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Medium (23.79%)
# Total Accepted:    246554
# Total Submissions: 1036425
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        buffer_dict = {}
        max_length = 0
        initial_curr = 0
        for pos, val in enumerate(s):
            if val not in buffer_dict:
                buffer_dict[val] = pos
            else:
                max_length = max(pos - initial_curr, max_length)
                buffer_dict = {va: po for (
                    va, po) in buffer_dict.items() if po > buffer_dict[val]}
                buffer_dict[val] = pos
                initial_curr = min(buffer_dict.values())
        return max(len(s) - initial_curr, max_length)
