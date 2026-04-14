class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def generate(nums, target, curr, result, max_count, index):
            if sum(curr) == target and len(curr) == max_count:
                result.append(curr[:])
                return
            if len(curr) > max_count :
                return
            if index >= len(nums):
                return
            if sum(curr) > target:
                return

            # exclude 
            generate(nums, target, curr, result, max_count, index + 1)

            # include
            curr.append(nums[index])
            generate(nums, target, curr, result, max_count, index + 1)
            curr.pop()

        def final_generation(max_count, target):
            nums = [1,2,3,4,5,6,7,8,9]
            result = []
            
            generate(nums, target, [], result, max_count, 0)
            
            return result

        return (final_generation(k, n))
        
        
                
        