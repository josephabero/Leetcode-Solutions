"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1

        for i in range(len(prices) - 1):
            # Evaluate Profit
            diff = prices[right] - prices[left]
            if diff > profit:
                profit = diff

            if prices[left] >= prices[right]:
                left = right
            right += 1
        
        return profit