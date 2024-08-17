class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        summ=0
        for i in range(len(s)):
            summ+=abs(i-t.index(s[i]))
        return summ
        