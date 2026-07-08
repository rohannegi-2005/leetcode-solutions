class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def sol(n):
            if n == 0 or n == 1:
                return n

            if dp[n] != -1:
                return dp[n]

            dp[n] = sol(n - 1) + sol(n - 2)
            return dp[n]

        return sol(n)