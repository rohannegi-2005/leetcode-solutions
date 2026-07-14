class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]
        def solve(index, amount):

            if index >= n:
                return 0

            if amount== 0:
                return 1

            if dp[index][amount] != -1:
                return dp[index][amount]

            take = 0
            if coins[index] <= amount:
                take = solve(index, amount - coins[index])

            notTake = solve(index+1, amount)

            dp[index][amount] = (take + notTake)
            return dp[index][amount]

        return solve(0, amount)

            

        