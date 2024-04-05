class Solution:
    def makeGood(self, s: str) -> str:
        l=[]
        for i in s:
            l.append(i)
            if len(l)>=2 and l[-1].lower()==l[-2].lower() and l[-1]!=l[-2]:
                l.pop()
                l.pop()
        return "".join(l)