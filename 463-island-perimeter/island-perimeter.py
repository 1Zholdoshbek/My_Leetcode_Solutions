class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count=0
        row=len(grid)
        columb=len(grid[0])
        if row==0:return 0
        for i in range(row):
            for j in range(columb):
                if grid[i][j]==1:
                    count+=4
                    if i-1>=0 and grid[i-1][j]==1:
                        count-=2
                    if j-1>=0 and grid[i][j-1]==1:
                        count-=2
        return count
        
        
        