#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii
#
# Medium (31.70%)
# Total Accepted:    107875
# Total Submissions: 332211
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
#
# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
#
#
# Each number in C may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
#
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
#


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        result = []
        curr_result = []
        candidates_new = sorted(candidates)
        self.combinationSumHelper(
            result, curr_result, candidates_new, target, 0)
        return result

    def combinationSumHelper(self, total_result, curr_result, candidates, target, start):
        if target == 0:
            total_result.append(curr_result)
            return
        i = start
        while i < len(candidates):
            if i > start and candidates[i] == candidates[i - 1]:
                i += 1
                continue
            if candidates[i] <= target:
                self.combinationSumHelper(
                    total_result, curr_result + [candidates[i]], candidates, target - candidates[i], i + 1)
            i += 1
