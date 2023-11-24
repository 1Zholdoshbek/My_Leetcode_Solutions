class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(32):
            cnt=0
            n=2**i
            for num in nums:
                if num & n:
                    cnt+=1
            if cnt>=k:
                ans+=n 
        return ans
                
        