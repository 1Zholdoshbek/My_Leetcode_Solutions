from queue import Queue
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[i+1 for i in range(n)]
        tmp=0
        while len(l)>1:
            tmp=(tmp+k-1)%len(l)
            l.pop(tmp)
        return l[0]
            
                
                
            
            