class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        curr_sum = 0
        for i in range(n):
            curr_sum = curr_sum + nums[i]
            output.append(curr_sum)

        return output

        