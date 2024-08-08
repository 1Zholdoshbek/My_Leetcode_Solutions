class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        for i in nums:
            if i%3!=0:
                cnt+=1 
        return cnt
        