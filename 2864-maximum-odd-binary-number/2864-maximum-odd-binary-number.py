class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        one=s.count('1')
        zeros=n-one
        return '1'*(one-1) +'0'*zeros+'1'
            
        
        