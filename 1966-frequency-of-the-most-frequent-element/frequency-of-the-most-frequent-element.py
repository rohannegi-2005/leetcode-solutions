class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0 
        window_sum = 0
        ans = 1

        for i in range(len(nums)):
            window_sum = window_sum + nums[i]

            while nums[i] * (i - left + 1) - window_sum > k:
                window_sum = window_sum - nums[left] 
                left = left + 1

            ans = max(ans, (i - left + 1))

        return ans