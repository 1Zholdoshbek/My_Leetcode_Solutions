class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ=bin(int(a,2)+int(b,2))
        return summ[2:]
        