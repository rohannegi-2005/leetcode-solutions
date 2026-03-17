class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def calculate(number):
            ans = 0
            for num in nums:
                ans = ans + (num + number - 1) // number

            return ans

        
        
        low = 1
        high = max(nums)
        
        while low < high:
            mid = (low + high) // 2
            # print(f"mid:{mid}")
            if calculate(mid) > threshold:
                low = mid + 1
                # print(f"low:{high}")
            else: 
                high = mid 
                # print(f"high:{low}")

        return low  


        