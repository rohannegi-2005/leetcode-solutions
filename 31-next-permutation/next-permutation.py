class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        store = 0
        switch = 0 
        for i in range (length-1,0,-1):
            if nums[i] > nums[i-1]:
                store = i -1 
                # print(store)
                switch = 1
                break
        # print(switch)

        if switch == 0:
            nums.reverse()
            
        else:
            for i in range (length-1,0,-1):
                if nums[i] > nums[store]:
                    temp = nums[i]
                    nums[i] = nums[store]
                    nums[store] = temp
                    nums[store+1:] = reversed(nums[store+1:])
                    break
                

                
            

        

        
        
        

        
                

            
            

        