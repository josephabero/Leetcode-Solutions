"""
Product Of Array Except Self
https://leetcode.com/problems/product-of-array-except-self
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)

        # Calculate prefix
        prefix = 1
        for i, num in enumerate(nums):
            answers[i] = prefix
            prefix *= num

        # Reverse Order, multiply previous prefix with postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= postfix
            postfix *= nums[i]

        return answers
