class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        y = 1
        x = 0
        length = len(s)
        count = 1
        max_len = 1

        if length == 0 or length == 1:
            return length

        while y < length:
            
            if s[y] not in s[x:x+count]:
                count = count + 1
                y = y + 1
                max_len = max(max_len, count)
            else:
                idx = s[x:x+count].index(s[y])
                x = x + idx + 1
                count = y - x + 1
                y = y + 1

        return max_len
                
                
                


        