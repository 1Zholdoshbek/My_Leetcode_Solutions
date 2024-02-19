class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        l=[]
        tmp=bin(n)[2:]
        for i in tmp:
            l.append(int(i))
        if sum(l)==1:
            return True
        return False
        