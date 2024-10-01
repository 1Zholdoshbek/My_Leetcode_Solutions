class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        return sum(arr)%k==0 and min(arr)<k/2 and max(arr)>k/2