class Solution:
    def check(self, nums: List[int]) -> bool:
        sorts=sorted(nums)
        nums+=nums
        if str(sorts)[1:-1] in str(nums):
            return True
        else:
            return False
            