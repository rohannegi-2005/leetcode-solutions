class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[None] * (n+1) for _ in range(n+1)]

        def solve(i, j):
            if i > j :
                return 0
            
            if dp[i][j] is not None:
                return dp[i][j]

            take_first = piles[i] - solve(i+1, j)

            take_last = piles[j] - solve(i, j-1)

            dp[i][j] =  max(take_first, take_last)

            return dp[i][j]

        return solve(0, n-1) > 0

    
        