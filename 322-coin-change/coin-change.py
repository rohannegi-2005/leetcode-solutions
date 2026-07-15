class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]
        def solve(amount, index):

            if index >= n or amount < 0 :
                return float('inf')

            if amount == 0 :
                return 0

            if dp[index][amount] != -1:
                return dp[index][amount]

            include = 1 + solve(amount-coins[index], index)

            exclude = solve(amount, index+1)


            dp[index][amount] =  min(include,exclude)
            return dp[index][amount]
            # return  min(include,exclude)

        ans =  solve(amount, 0 )

        if ans == float('inf'):
            return -1
        else:
            return ans


            


        