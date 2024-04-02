class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        dict={}
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in dict.values():
                    return False
                dict[s[i]]=t[i]
        return True
            