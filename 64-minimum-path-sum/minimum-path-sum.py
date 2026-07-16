class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        dp = [[-1] * column for _ in range(row)]

        def solve(i, j):
            if i == row-1 and j == column-1:
                return grid[i][j]

            if i >= row or j >= column:
                return float(inf)

            if dp[i][j] != -1:
                return dp[i][j]

            move_right = grid[i][j] + solve(i+1, j)
            move_bottom = grid[i][j] + solve(i, j+1)

            dp[i][j] =  min(move_right, move_bottom)
            return dp[i][j]

        return solve(0,0)

            

            
        