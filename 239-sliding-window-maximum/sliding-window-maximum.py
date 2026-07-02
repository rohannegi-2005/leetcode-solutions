from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        stack = deque()
        n = len(nums)
        j = 0
        for i in range(n):
             
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if not stack :
                stack.append(i)
            elif nums[stack[-1]] >= nums[i] :
                stack.append(i)
 
            if i - j + 1 >= k:
                answer.append(nums[stack[0]])
                j = j + 1
                if stack[0] < j:
                    stack.popleft()
            # print(stack)
            # print(answer)
                

        return answer
