# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        pre=None
        c=head
        while c:
            t=c.next
            c.next=pre
            pre=c
            c=t
        head=pre
        return head
        