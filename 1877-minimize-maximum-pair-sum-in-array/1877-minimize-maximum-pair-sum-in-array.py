class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxx=nums[0]
        nums.sort()
        i=0
        j=len(nums)-1
        while i<=j:
            tmp=nums[i]+nums[j]
            if tmp>maxx:
                maxx=tmp
            i+=1
            j-=1
        return maxx
                
            
        