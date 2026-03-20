class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()   # ✅ important

        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])   # odd
        else:
            return (nums[n//2 - 1] + nums[n//2]) / 2.0   # even