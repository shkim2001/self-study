class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return
    
    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next