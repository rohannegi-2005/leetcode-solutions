class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        maximum = max(nums)
        for i in range(0,length,1):
            if nums[i] == maximum:
                return i

        