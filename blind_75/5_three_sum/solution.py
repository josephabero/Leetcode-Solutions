"""
3Sum
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        sol = []
        
        for i, num in enumerate(s_nums):
            # Avoid duplicate entries
            if i > 0 and num == s_nums[i - 1]:
                continue

            left = i + 1
            right = len(s_nums) - 1
            
            while(left < right):
                three_sum = num + s_nums[left] + s_nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    sol.append([num, s_nums[left], s_nums[right]])
                    left += 1
                    while s_nums[left] == s_nums[left - 1] and left < right:
                        left += 1
                        
        return sol