class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def generate(nums, current, index, result):
            nums.sort()
            if index >= len(nums):
                result.append(current[:])
                return

            # Exclude
            next_index = index
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index = next_index + 1
            generate(nums, current, next_index, result)

            # include
            current.append(nums[index])
            generate(nums, current, index + 1, result)
            current.pop()

        def subsets_2(nums):
            result = []
            generate(nums, [], 0, result)
            return result

        return (subsets_2(nums))


        