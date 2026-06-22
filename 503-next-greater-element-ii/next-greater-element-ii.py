from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums = nums + nums
        n = len(nums)
        result = [-1] * n
        stack = deque()
        
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]
            stack.append(i)

        return result[:length]

        
        
        