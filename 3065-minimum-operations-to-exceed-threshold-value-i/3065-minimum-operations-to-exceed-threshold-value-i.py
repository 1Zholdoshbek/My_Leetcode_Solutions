class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt=0
        for i in nums:
            if k>i:
                cnt+=1
                continue
        return cnt
        
        