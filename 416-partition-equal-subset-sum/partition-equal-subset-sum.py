class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [[None] * (target+1) for _ in range(n+1)]

        def solve(index, target):
            
            if index == n:
                return False

            if target == 0:
                return True

            if dp[index][target] is not None:
                return dp[index][target]

            take = 0
            if nums[index] <= target:
                take = solve(index+1, target-nums[index])

            notTake = solve(index+1, target)

            dp[index][target] = take or notTake
            return dp[index][target]

        return solve(0, target)

        