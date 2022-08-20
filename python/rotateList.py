# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0 or head is None or head.next is None:
            return head
        curr = head
        i = 2
        while curr.next.next is not None:
            curr = curr.next
            i+=1 
        if k > i and k % i > 0:
            k = k % i         
        last = curr.next
        curr.next = None
        last.next = head
        return self.rotateRight(last, k-1)