# class Solution:
#     def countGoodNumbers(self, n: int) -> int:
#         def function(n):
#             MOD = 10**9 + 7
#             if n == 0 :
#                 return 1
#             if n % 2 == 0 :
#                 return (4 * function(n-1)) % MOD
#             else:
#                 return (5 * function(n-1)) % MOD


#         answer = function(n)
#         return answer 

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, y):
            result = 1
            x = x % MOD
            
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                y //= 2
            
            return result
        
        even = (n + 1) // 2
        odd = n // 2
        
        return (power(5, even) * power(4, odd)) % MOD


        