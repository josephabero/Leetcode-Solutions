"""
Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        sorted_counts = [[] for i in range(0, len(nums) + 1)]
        for num, count in counts.items():
            sorted_counts[count].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for element in sorted_counts[i]:
                if len(result) == k:
                    return result
                result.append(element)

        return result
