class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans=[]
        for i in range(k):
            tmp = min(nums)*multiplier
            index=nums.index(min(nums))
            nums[index]=tmp
            print(nums)
        return nums
            