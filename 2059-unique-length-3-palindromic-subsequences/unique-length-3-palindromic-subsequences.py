class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        m={}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=[]
            m[s[i]].append(i)
        n=set()
        res=0
        for i in m:
            if len(m[i])>=2 and m[i][-1]-m[i][0]>1:
                res+=len(set(s[m[i][0]+1:m[i][-1]]))
        return res