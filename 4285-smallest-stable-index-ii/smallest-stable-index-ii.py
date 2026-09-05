class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)

        max_prefix = [nums[0]] * n
        min_suffix = [nums[n-1]] * n

        for i in range(1, n):
            if max_prefix[i-1] <= nums[i]:
                max_prefix[i] = nums[i]
            else:
                max_prefix[i] = max_prefix[i-1]

        for i in range(n-2,-1,-1):
            if min_suffix[i+1] >= nums[i]:
                min_suffix[i] = nums[i]
            else:
                min_suffix[i] = min_suffix[i+1]

        for i in range(n):
            check = max_prefix[i] - min_suffix[i]
            if check <= k:
                return i

        return -1





        
        