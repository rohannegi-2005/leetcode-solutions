# class Solution:
#     def minimumSubstringsInPartition(self, s: str) -> int:

#         n = len(s)

#         def check_balanced(s):
#             dictionary = {}

#             for ch in s:
#                 dictionary[ch] = dictionary.get(ch, 0) + 1

#             return len(set(dictionary.values())) <= 1

#         dp = [None] * (n+1)

#         def solve(i):
#             if i == n:
#                 return 0

#             if dp[i] is not None:
#                 return dp[i] 

#             ans = float("inf")
            
#             for j in range(i,n):
#                 if check_balanced(s[i:j+1]):
#                     ans = min(ans, 1 + solve(j+1))

#             dp[i] = ans
#             return dp[i]


#         return solve(0)

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        dp = [None] * (n + 1)

        def solve(i):
            if i == n:
                return 0

            if dp[i] is not None:
                return dp[i]

            freq = [0] * 26
            ans = float("inf")

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                # Check if current substring is balanced
                target = 0
                balanced = True

                for f in freq:
                    if f == 0:
                        continue
                    if target == 0:
                        target = f
                    elif f != target:
                        balanced = False
                        break

                if balanced:
                    ans = min(ans, 1 + solve(j + 1))

            dp[i] = ans
            return ans

        return solve(0)
            
        
    