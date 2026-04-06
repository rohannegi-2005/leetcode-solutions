class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def generate(k, nums, result, current, index):
            if sum(current) > k:
                return
            if sum(current) == k:
                result.append(current[:])
                return
            if index >= len(nums):
                return
            

            # Exclude the current element
            generate(k, nums, result, current, index + 1)

            # Include the current element
            current.append(nums[index])
            generate(k, nums, result, current, index )
            # generate(k, nums, result, current, index + 1)
            current.pop()
            

        def find_combinations(target, candidates):
            result = []
            generate(target, candidates, result, [], 0)
            return result

        result = find_combinations(target,candidates)
        return result

        
                    

            
        