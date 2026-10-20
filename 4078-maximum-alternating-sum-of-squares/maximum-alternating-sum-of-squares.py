class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        length = len(nums)

        for i in range(length):
            nums[i] = nums[i]**2

        nums.sort(reverse = True)
        answer = 0
        x = 0
        y = length - 1

        for i in range(length):
            if i % 2 == 0:
                answer = answer + nums[x]
                x = x + 1
            else:
                answer = answer - nums[y]
                y = y - 1


        return answer







        