class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate(index, current):

            if index == len(nums):
                result.append(current)
                return

            # Exclude
            generate(index + 1, current)

            # Include
            generate(index + 1, current + [nums[index]])

        result = []
        generate(0, [])
        return result
        
        