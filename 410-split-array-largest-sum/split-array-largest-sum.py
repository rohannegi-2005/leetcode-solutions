class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def issplit(k,nums,max_sum):
            curr_sum = 0 
            count = 1
            for num in nums:
                if curr_sum + num <= max_sum:
                    curr_sum = curr_sum + num
                else:
                    count = count + 1
                    curr_sum = num

            if count <= k:
                return True

            else:
                return False


        low = max(nums)
        high = sum(nums)

        while low < high:
            
            mid = (low + high) // 2

            if issplit(k,nums,mid):
                high = mid

            else:
                low = mid + 1

        return low

            
        