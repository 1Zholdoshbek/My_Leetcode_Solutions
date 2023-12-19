# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        l=[]
        pos=0
        while list1:
            if  pos==a:
                while True:
                    while list2:
                        l.append(list2.val)
                        list2=list2.next
                    
                    if pos==b:
                        list1=list1.next
                        break

                    list1=list1.next
                    pos+=1
            l.append(list1.val)
            list1=list1.next
            pos+=1
        d=n=ListNode()
        for i in l:
            d.next=ListNode(i)
            d=d.next
        return n.next
                        
                        
                    