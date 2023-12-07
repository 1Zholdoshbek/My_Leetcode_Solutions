class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for i in range(0,len(words),1):
            if x in words[i]:
                l.append(i)
        return l
        