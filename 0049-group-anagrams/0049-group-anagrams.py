class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp=defaultdict(list)
        
        for i in strs:
            tmp[frozenset(Counter(i).items())].append(i)
        return tmp.values()
        