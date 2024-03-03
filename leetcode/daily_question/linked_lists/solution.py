from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    new_list = ListNode()
    new_list.next = head
    pointer1 = head

    while n:
        pointer1=pointer1.next
        n-=1
        
    pointer2=new_list
    while pointer1:
        pointer2=pointer2.next
        pointer1=pointer1.next

    pointer2.next = pointer2.next.next
    return new_list.next