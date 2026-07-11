class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        def generateWays(i,j):

            if i >= m or j >= n:
                return 0 

            if obstacleGrid[i][j] == 1:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            down = generateWays(i+1, j)
            right = generateWays(i, j+1)

            dp[i][j] =  down + right

            return dp[i][j]

        return generateWays(0,0)