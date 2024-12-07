class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def jooptor(nums,maxOperations,a):
            return sum((num+a-1)//a-1 for num in nums)<=maxOperations
        left,right=1,max(nums)
        while left<=right:
            mid=left+(right-left)//2
            if jooptor(nums,maxOperations,mid):
                right=mid-1
            else:
                left=mid+1
        return left