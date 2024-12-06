class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        
        current_sum = 0
        count = 0
        
        for num in range(1, n + 1):
            if num in banned_set or current_sum + num > maxSum:
                continue
            
            current_sum += num
            count += 1
        
        return count