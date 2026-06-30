from collections import deque

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        MOD = 10**9 + 7
        stack = deque()
        previous_smaller = [-1] * n
        next_smaller = [n] * n

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)
       
        stack = deque()
        
        for i in range(n-1,-1,-1):
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                previous_smaller[idx] = i
            stack.append(i)
        
        for i in range(n):
            count = count +  ((i - previous_smaller[i]) * (next_smaller[i] - i)) * arr[i]
            count = count % MOD


        return count 
    