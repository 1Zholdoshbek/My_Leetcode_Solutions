# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        next=head.next
        while next!=None:
            tmp=ListNode(math.gcd(head.val,next.val))
            head.next=tmp
            tmp.next=next
            head=next
            next=next.next
        return h
            
        
            
        