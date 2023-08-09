class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        count=0
        while len(grid[0]):
            tmp = 0
            i = 0
            while i < len(grid):
                g = max(grid[i])
                if g > tmp:
                    tmp = g
                grid[i].remove(g)
                i += 1
            count += tmp
        return count