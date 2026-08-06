class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [None] * (n+1)

        def solve(i):
            if i == n:
                return 0

            if dp[i] is not None:
                return dp[i]

            curr_max = 0
            ans = 0

            for j in range(i, min(n, i+k)):
                curr_max = max(curr_max, arr[j])
                length = j - i + 1

                ans = max(ans, curr_max * length + solve(j+1))

            dp[i] = ans
            return dp[i]


        return solve(0)
        