class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            if num in pairs:
                return pairs[num], i
            pairs[target - num] = i
            