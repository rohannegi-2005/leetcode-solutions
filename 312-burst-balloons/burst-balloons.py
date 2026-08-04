class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums.insert(0, 1)
        nums.append(1)

        n = len(nums)

        dp = [[None] * (n+1) for _ in range(n+1)]

        def solve(i, j):
            if i > j :
                return 0 

            if dp[i][j] is not None:
                return dp[i][j]

            max_cost = float("-inf")
            cost = 0
            
            for index in range(i, j+1):
                cost = (nums[i-1] * nums[index] * nums[j+1]) + solve(i, index-1) + solve(index+1, j)

                max_cost = max(max_cost, cost)

            dp[i][j] = max_cost

            return dp[i][j]


        return solve(1, n-2)


            

        