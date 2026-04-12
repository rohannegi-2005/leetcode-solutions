class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate(nums, current, index, result):
            if index >= len(nums):
                result.append(current[:])
                return

            # Exclude
            generate(nums, current, index + 1, result)

            # include
            current.append(nums[index])
            generate(nums, current, index + 1, result)
            current.pop()

        def subsets_2(nums):
            result = []
            generate(nums, [], 0, result)
            return result

        return (subsets_2(nums))
        