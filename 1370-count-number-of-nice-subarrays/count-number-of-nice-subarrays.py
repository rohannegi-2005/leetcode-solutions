class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        prefix_map = {0: 1}   
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]

            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count
        



        