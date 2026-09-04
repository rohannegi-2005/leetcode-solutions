class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        stable = 0
        mini = float('inf')
        ans = -1

        for i in range(n):
            stable = max(nums[:i+1]) - min(nums[i:])

            if stable <= k and mini > stable:   
                mini = stable
                ans = i
                break

        return ans



        