from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k = k - 1
            stack.append(digit)


        while k > 0 :
            stack.pop()
            k = k - 1

        result = ''.join(stack).lstrip('0')

        return result if result else "0"
                
            



        
        