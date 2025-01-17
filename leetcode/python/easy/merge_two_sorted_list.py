from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:Optional[ListNode] = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        resultList = ListNode()

        it1 = list1
        it2 = list2

        it = resultList

        while True:
            if not it1:
                it.next = it2
                it = it.next
                break

            if not it2:
                it.next = it1
                it = it.next
                break

            if it1.val > it2.val:
                it.next = it1
                it = it.next
                it1 = it1.next
                continue

            if it1.val < it2.val:
                it.next = it2
                it = it.next
                it2 = it2.next
                continue

            if it2.val == it1.val:
                it.next = it2
                it = it.next
                it2 = it2.next

                it.next = it1
                it = it.next
                it1 = it1.next
                continue

        return resultList.next
