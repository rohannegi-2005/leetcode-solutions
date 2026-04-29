class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        count = 0
        zero = 0
        zero_index = []
        j = 0
        max_count = 0
        for i in range(0,length):
            if nums[i] == 1 :
                count = i - j + 1
            if nums[i] == 0:
                zero = zero + 1
                zero_index.append(i)
            if nums[i] == 0 and zero <= k:
                count = i - j + 1
            if (nums[i] == 0) and (zero > k):
                j = zero_index[0] + 1
                del zero_index[0]
                count = i - j + 1

            max_count = max(max_count, count)
            

        return max_count
            
        