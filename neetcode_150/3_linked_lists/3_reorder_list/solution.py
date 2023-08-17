"""
Reorder List
https://leetcode.com/problems/reorder-list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find middle, then split the list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        list2 = slow.next
        slow.next = None

        # Reverse the second list
        prev, curr = None, list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Merge the two lists
        list1, list2 = head, prev
        new_head = ListNode(0, None)
        curr = new_head

        while list1 or list2:
            if list1:
                # Add list1 node to result list
                curr.next = list1
                curr = list1
                list1 = list1.next

            if list2:
                # Add list2 node to result list
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        return new_head.next
