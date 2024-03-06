# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first,second=head,head;
        while first and first.next:
            first,second=first.next.next,second.next
            if first==second:
                return True
        return False
        