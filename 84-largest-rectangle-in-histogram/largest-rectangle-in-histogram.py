from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Next Smaller Element
        next_smaller = [n] * n
        stack = deque()
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)
        print(next_smaller)

        # Previous Smaller Element
        prev_smaller = [-1] * n
        stack = deque()
        for i in range(n-1,-1,-1):
            while stack and heights[i] <= heights[stack[-1]]:
                idx = stack.pop()
                prev_smaller[idx] = i
            stack.append(i)
        print(prev_smaller)

        # Area
        max_area = 0
        for i in range(n):
            height = heights[i]
            width = next_smaller[i] - prev_smaller[i] - 1
            area = height * width 
            max_area = max(max_area, area)

        
        return max_area
