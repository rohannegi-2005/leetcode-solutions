class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [None] * (n+1)
        
        def solve(x):
            if x == 1:
                return 1

            if dp[x] is not None:
                return dp[x]

            ans = 0

            for i in range(1, x):
                ans = max(ans, i * (x-i), i * solve(x-i))

            dp[x] = ans
            return dp[x]

        return solve(n)
    

        
        