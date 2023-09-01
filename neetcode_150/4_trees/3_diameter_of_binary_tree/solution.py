"""
Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        max_diameter = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            max_diameter[0] = max(max_diameter[0], left + right + 2)

            return max(left, right) + 1

        dfs(root)

        return max_diameter[0]
