class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans=[i for i in nums if i<pivot]
        ans.extend([pivot]*nums.count(pivot))
        ans.extend([i for i in nums if i>pivot])
        return ans