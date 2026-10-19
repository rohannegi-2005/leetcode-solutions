class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
            elif nums[i] > target:
                return answer

        return answer
        