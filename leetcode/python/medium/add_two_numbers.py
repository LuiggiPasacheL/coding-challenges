from typing import Optional

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2

        if not l2:
            return l1

        initial = ListNode()

        result = initial

        carry = 0

        while(l1 != None and l2 != None and carry != 0):

            value1 = 0
            if l1 != None:
                value1 = l1.val

            value2 = 0
            if l2 != None:
                value2 = l2.val

            sum = value1 + value2 + carry

            val = 0
            if (sum > 10):
                carry = 1
                val = sum - 10
                result = result.next
            else:
                carry = 0
                val = sum
                result = result.next

            result = ListNode(val=val)

        return initial.next

