class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_indices = []
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_indices.append(right)

            if len(zero_indices) > k:
                left = zero_indices.pop(0) + 1

            max_length = max(max_length, right - left + 1)

        return max_length