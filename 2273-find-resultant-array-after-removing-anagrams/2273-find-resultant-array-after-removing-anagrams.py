class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=0
        while True:
            if i==len(words)-1:
                break
            if ''.join(sorted(words[i]))==''.join(sorted(words[i+1])):
                words.pop(i+1)
                i-=1
            i+=1
        return words