class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        store = 0

        # # Base Case
        # if n == 1:
        #     return True

        for i in range(n):
            if i <= store:
                store = max(i+nums[i], store)
                print(store)
          
        if store >= n-1:
            return True
        else:
            return False
            
