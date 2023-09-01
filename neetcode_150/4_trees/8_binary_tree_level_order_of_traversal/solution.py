"""
Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        tree = []

        while queue:
            length = len(queue)

            nodes = []
            for i in range(length):
                node = queue.popleft()
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if nodes:
                tree.append(nodes)

        return tree
