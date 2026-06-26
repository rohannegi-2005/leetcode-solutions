class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        nums = list(set(nums))
        nums.sort()

        n = len(nums)
        if n == 1:
            return 1

        count = 1
        max_count = 0

        for i in range (1,n):
            if nums[i] == nums[i-1] + 1:
                count = count + 1
            else:
                count = 1
            max_count = max(max_count, count)

        return max_count





        