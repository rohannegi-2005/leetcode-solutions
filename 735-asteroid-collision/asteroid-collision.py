class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)

        for i in range(n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else: 
                while stack and asteroids[i] * (-1) > stack[-1] > 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                if asteroids[i] * (-1) == stack[-1] > 0:
                    stack.pop()

        return stack
              