#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum
#
# Medium (36.23%)
# Total Accepted:    149617
# Total Submissions: 402233
# Testcase Example:  '[2,3,6,7]\n7'
#
#
# Given a set of candidate numbers (C) (without duplicates) and a target number
# (T), find all unique combinations in C where the candidate numbers sums to
# T.
#
#
# The same repeated number may be chosen from C unlimited number of times.
#
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
#
# [
# ⁠ [7],
# ⁠ [2, 2, 3]
# ]
#
#
#


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        result = []
        curr_result = []
        self.combinationSumHelper(result, curr_result, candidates, target, 0)
        return result

    def combinationSumHelper(self, total_result, curr_result, candidates, target, start):
        if target == 0:
            total_result.append(curr_result)
            return
        i = start
        while i < len(candidates):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= target:
                self.combinationSumHelper(
                    total_result, curr_result + [candidates[i]], candidates, target - candidates[i], i)
            i += 1
