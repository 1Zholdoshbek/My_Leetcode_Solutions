class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        i=0
        j=1
        while j<len(nums):
            l.append(nums[j])
            l.append(nums[i])
            i+=2
            j+=2 
        return l
            