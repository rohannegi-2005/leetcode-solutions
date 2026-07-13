class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        def costs(index):

            if index >= n:
                return 0

            if dp[index] != -1:
                return dp[index]
                
            # one step 
            onestepCost = cost[index] + costs(index+1)

            # two step 
            twostepCost = cost[index] + costs(index+ 2)

            dp[index] =  min(onestepCost, twostepCost)

            return dp[index]

        return min(costs(0), costs(1))
        