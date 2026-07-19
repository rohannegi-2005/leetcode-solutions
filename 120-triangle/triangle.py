class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None] * n for _ in range(n)]

        def solve(i, j):
            if i == n - 1:
                return triangle[i][j]

            if dp[i][j] is not None:
                return dp[i][j]

            dp[i][j] = triangle[i][j] + min(
                solve(i + 1, j),
                solve(i + 1, j + 1)
            )

            return dp[i][j]

        return solve(0, 0)