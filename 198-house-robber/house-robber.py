class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * (n+1)

        def solve(nums, index,n,dp):

            if index >= n:
                return 0

            if dp[index] != -1:
                return dp[index]

            not_take = solve(nums, index + 1, n, dp)
            take = nums[index] + solve(nums, index+ 2, n, dp)

            dp[index] = max(take, not_take)
            return dp[index]

        return solve(nums, 0, n,dp)


        