class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n  = len(nums)
        print(nums)

        count = 0
        for i in range(n-1,-1,-1):
            if i < n - 1 and nums[i] == nums[i + 1]:
                    continue
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff == k:
                    count = count + 1
                    break

        return count


        

            

        
        

            