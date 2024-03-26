class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                l.append(nums[i])
        return l[0]
        