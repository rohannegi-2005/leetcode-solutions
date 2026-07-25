class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [[None] * (target + 1) for _ in range(n+1)]

        def solve(index, target):
            if index >= n :
                if target == 0:
                    return 0
                return -float("inf")

            if dp[index][target] is not None:
                return dp[index][target]

            take = -float("inf")
            if target >= nums[index]:
                take = 1 + solve(index+1, target - nums[index])

            notTake = solve(index+1, target)

            dp[index][target] = max(take, notTake)
            return dp[index][target]

        output = solve(0, target)

        if output > 0:
            return output 
        else:
            return -1
        