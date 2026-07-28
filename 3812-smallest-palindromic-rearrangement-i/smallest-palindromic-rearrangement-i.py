# class Solution:
#     def smallestPalindrome(self, s: str) -> str:

#         dictionary = {}
#         n = len(s)
#         mid = n // 2

#         start = 0
#         end = n - 1

#         for i in s:

#             if i in dictionary:
#                 dictionary[i] = dictionary[i] + 1
#             else:
#                 dictionary[i] = 1


#         dictionary = dict(sorted(dictionary.items()))


#         ans = [""] * n

#         for key in dictionary.keys():
#             print(key)
#             if dictionary[key] % 2 != 0:
#                 ans[mid] = key
#                 dictionary[key] = dictionary[key] - 1

#             for count in range(dictionary[key] // 2):
#                 ans[start] = key
#                 ans[end] = key
#                 dictionary[key] = dictionary[key] - 2
#                 start = start + 1
#                 end = end - 1

#         ans = "".join(ans)
        
#         return ans

from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        n = len(s)
        ans = [""] * n

        start = 0
        end = n - 1
        mid = n // 2

        for ch in sorted(freq.keys()):
            count = freq[ch]

            # Place the middle character (if odd frequency)
            if count % 2 == 1:
                ans[mid] = ch

            # Place pairs from both ends
            pairs = count // 2
            for _ in range(pairs):
                ans[start] = ch
                ans[end] = ch
                start += 1
                end -= 1

        return "".join(ans)
                


            



        
        