class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        dp = [None] * (n+1)

        def solve(i):
            if i == n:
                return 0

            if dp[i] is not None:
                return dp[i]

            min_cut = float("inf")
            cut = 0
            for index in range(i,n):
                if s[i:index+1] == s[i:index+1][::-1]:
                    cut = 1 + solve(index+1)
                    min_cut = min(min_cut, cut)

            dp[i] = min_cut
            return dp[i]


        return solve(0) - 1

        