# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         string = ""
#         count = 0
#         length = len(s)
#         for i in range(length-2):
#             string = s[i:i+3]
#             # print(string)
#             if "a" in string and "b" in string and "c" in string:
#                     count = count + 1
#             for j in range(i+3,length):
#                 string = string + s[j]
#                 # print(string)
#                 if "a" in string and "b" in string and "c" in string:
#                     count = count + (length - j)
#                     break
                
#         return count

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        freq = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        left = 0
        count = 0
        length = len(s)

        for right in range(length):

            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:

                count += (length - right)

                freq[s[left]] -= 1
                left += 1

        return count
