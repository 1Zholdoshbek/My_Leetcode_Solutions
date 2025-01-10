class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:


        max_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char, freq in word_freq.items():
                max_freq[char] = max(max_freq[char], freq)
        
       
        ans = []
        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                ans.append(word)
        
        return ans

                
        