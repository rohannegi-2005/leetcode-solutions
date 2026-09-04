class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        stable = 0

        for i in range(n):
            stable = max(nums[:i+1]) - min(nums[i:])

            if stable <= k :  
                return i 

        return -1



        