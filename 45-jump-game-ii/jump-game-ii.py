class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        curr = 0
        farthest = 0
        jumps = 0
        

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == curr:
                jumps = jumps + 1
                curr = farthest

        return jumps



        