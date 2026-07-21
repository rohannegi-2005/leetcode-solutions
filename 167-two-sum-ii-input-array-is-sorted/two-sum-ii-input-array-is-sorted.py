class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sums = 0

        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left+1, right+1]

            elif sums > target:
                right = right - 1

            else:
                left = left + 1


        