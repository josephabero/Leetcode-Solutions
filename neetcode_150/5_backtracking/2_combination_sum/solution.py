"""
Combination Sum
https://leetcode.com/problems/combination-sum/
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, combination, total):
            if total == target:
                result.append(combination.copy())
                return

            if i >= len(candidates) or total > target:
                return

            dfs(i, combination + [candidates[i]], total + candidates[i])
            dfs(i + 1, combination, total)

        dfs(0, [], 0)
        return result
