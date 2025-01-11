class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split("-")
        s=""
        for i in l:
            s=s+bin(int(i))[2:]+"-"
        return s[:len(s)-1:]

        