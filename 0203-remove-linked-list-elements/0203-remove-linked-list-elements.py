# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        while head and head.val==val:
            head=head.next
        if head==None:
            return head
        p=head
        c=head.next
        while c:
            if c.val==val:
                p.next=c.next
                c=c.next
            else:
                p=c
                c=c.next
        
        return head