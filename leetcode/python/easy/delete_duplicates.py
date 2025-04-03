from typing import Optional, List
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list_node(lst: List) -> Optional[ListNode]:

    head = ListNode()
    aux = head

    for e in lst:
        aux.next = ListNode(val=e)
        aux = aux.next

    return head.next

def node_to_list(head: Optional[ListNode]) -> List[None]:

    lst = []

    aux = head
    while(aux):
        lst.append(aux.val)
        aux = aux.next

    return lst


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        map_values = {}

        if not head:
            return head

        aux = head
        map_values[aux.val] = True

        while aux.next:

            if aux.next.val not in map_values:
                map_values[aux.next.val] = True
                aux = aux.next
            else:
                aux.next = aux.next.next


        if aux and aux.val in map_values:
            aux.next = None

        return head


head = create_list_node([1,1,1])
print(node_to_list(Solution().deleteDuplicates(head)))

