class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(column):
                if grid[i][j] < 0:
                    count = count + 1


        return count
        
        