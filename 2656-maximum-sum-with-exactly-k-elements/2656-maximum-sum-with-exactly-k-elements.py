class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        summ=0
        nums.sort()
        l=len(nums)
        tmp=nums[l-1]
        for i in range(k):
            summ+=tmp
            tmp+=1
        return summ