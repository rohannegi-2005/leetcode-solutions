class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def solve(nums):
            n = len(nums)
            dp = [-1] * n

            def helper(index):
                if index >= n:
                    return 0

                if dp[index] != -1:
                    return dp[index]
            
                not_take = helper(index+1)
                take = nums[index] + helper(index+2)

                dp[index] = max(take,not_take)

                return dp[index]

            return helper(0)

        # case 1 -> exclude 1st index
        case1 = solve(nums[1:])

        # case 2 -> exclude 2nd index
        case2 = solve(nums[:-1])

        return max(case1,case2)

        
            

            
            
        