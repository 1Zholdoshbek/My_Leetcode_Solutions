class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        t=Counter(arr)
        t=dict(t)
        print(t)
        maxx=max(t.values())
        l=[i for i in t if t[i]==maxx]
        return l[0]
        