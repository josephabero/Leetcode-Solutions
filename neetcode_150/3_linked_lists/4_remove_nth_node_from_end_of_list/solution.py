"""
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Neetcode Solution: Uses 2 pointers (O(n))
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left, right = dummy, head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        # Remove target node
        left.next = left.next.next

        return dummy.next


# Own solution: Get length, iterate through. O(2n)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = head
        length = 0
        while tail:
            tail = tail.next
            length += 1

        # 0 indexing
        target = length - n

        # Handle when first index is removed (includes size 1 lists)
        if target == 0:
            return head.next

        node = head
        for i in range(target):
            # Stop at node prior to node to be removed
            if i == (target - 1):
                # Remove node
                target_node = node.next
                node.next = target_node.next
                target_node.next = None
                break
            node = node.next

        return head
