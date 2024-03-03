# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        jay=yldam=head
        for _ in range(n):
            yldam=yldam.next
        if not yldam:
            return head.next
        while yldam.next:
            yldam=yldam.next
            jay=jay.next
        jay.next=jay.next.next
        return head
            
            