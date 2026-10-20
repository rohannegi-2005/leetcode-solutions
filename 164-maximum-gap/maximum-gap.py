class Solution:
    def maximumGap(self, nums: list[int]) -> int:

        length = len(nums)

        if length <= 1:
            return 0

        nums.sort()
        diff = 0
        answer = 0

        for i in range(1,length):
            diff = nums[i] - nums[i-1] 
            answer = max(answer, diff)

        return answer


        