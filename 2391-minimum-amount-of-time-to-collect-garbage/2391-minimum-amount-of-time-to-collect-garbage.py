class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        m=0
        p=0
        g=0
        ans=0
        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                m=i 
            if 'P' in garbage[i]:
                p=i 
            if 'G' in garbage[i]:
                g=i 
            ans+=len(garbage[i])
        ans+=sum(travel[:m])+sum(travel[:p])+sum(travel[:g])
        return ans
        