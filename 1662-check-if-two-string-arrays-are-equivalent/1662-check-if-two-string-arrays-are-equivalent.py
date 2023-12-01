class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        s2=""
        for i in word1:
            s+=i
        for i in word2:
            s2+=i
        if s==s2:
            return True
            return False
        