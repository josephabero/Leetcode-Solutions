"""
Add Two Numbers
https://leetcode.com/problems/add-two-numbers
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy =  ListNode(0, None)
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
        	# Get values
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            # Calculate total
            total = num1 + num2 + carry
            carry = total // 10

            # Only save ones place value
            curr.next = ListNode(total % 10)

            # Increment pointers
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next
