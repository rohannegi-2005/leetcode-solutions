class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def solve(index, target):
            if index == n: 
                if target == 0:
                    return 1
                else:
                    return 0 
            
            if (index, target) in dp:
                return dp[(index, target)]

            pos = solve(index + 1, target - nums[index])
            neg = solve(index + 1, target + nums[index])

            dp[(index, target)] =  pos + neg
            return dp[(index, target)]

        return solve(0, target)
            


        