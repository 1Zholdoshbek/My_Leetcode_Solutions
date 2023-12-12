class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tmp=0
        ans=0
        for i in nums:
            tmp+=i
            ans=min(ans,tmp)
        return -ans+1
                
        
        