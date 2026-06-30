from collections import deque

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        previous_great = [-1] * n
        previous_smaller = [-1] * n
        next_great = [n] * n
        next_smaller = [n] * n

        stack = deque()

        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)
        # print(next_smaller)

        stack = deque()
        for i in range(n-1,-1,-1):
            while stack and nums[i] <= nums[stack[-1]]:
                idx = stack.pop()
                previous_smaller[idx] = i
            stack.append(i)

        # print(previous_smaller)

        stack = deque()
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                next_great[idx] = i
            stack.append(i)
        # print(next_great)

        stack = deque()
        for i in range(n-1,-1,-1):
            while stack and nums[i] >= nums[stack[-1]]:
                idx = stack.pop()
                previous_great[idx] = i
            stack.append(i)
        # print(previous_great)

        sum_small = 0
        sum_large = 0
        for i in range(n):
            sum_small = sum_small + ((i - previous_smaller[i]) * (next_smaller[i] - i)) * nums[i]
            sum_large = sum_large + ((i - previous_great[i]) * (next_great[i] - i)) * nums[i]

        # print(sum_small)
        # print(sum_large)
            
        count = sum_large - sum_small

        return count
  