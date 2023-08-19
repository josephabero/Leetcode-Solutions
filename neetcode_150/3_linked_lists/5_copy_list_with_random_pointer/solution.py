"""
Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Initialize copied list
        curr = head

        # Iterate through dictionary and copy linked list
        copy_mapping = {}
        while curr:
            # Cache random node
            copied_node = Node(curr.val)
            copy_mapping[curr] = copied_node

            curr = curr.next

        # Assign pointers for random indexes
        curr = head
        while curr:
            copy = copy_mapping[curr]
            copy.next = copy_mapping.get(curr.next, None)
            copy.random = copy_mapping.get(curr.random, None)
            curr = curr.next

        return copy_mapping.get(head, None)
