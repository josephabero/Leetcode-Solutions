"""
Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Iteratively
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = tail = ListNode(0)
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return result.next


# Recursively
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def mergeLists(result, list1, list2):
            if list1 is None or list2 is None:
                if list1:
                    result.next = list1
                else:
                    result.next = list2
                return result
            
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            
            result = result.next
            
            mergeLists(result, list1, list2)
            
        result = tail = ListNode(0)
        mergeLists(tail, list1, list2)
        
        return result.next