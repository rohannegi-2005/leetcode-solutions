class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.append(0)
        left = 0 
        right = sum(nums) - nums[0]

        n = len(nums)

        # for i in range(n):

        #     for j in range(i+1,n):
        #         right = right + nums[j]
        #     for z in range(0,i):
        #         left = left + nums[z]
        #     if left == right :
        #         return i
            
        #     right = 0 
        #     left = 0
        # return -1

        for i in range(n-1):
            print(f"left:{left}")
            print(f"right:{right}")
            print("--------------------")
            if left == right:
                return i
            left = left + nums[i]
            right = right - nums[i+1] 
            
        return -1

            
        