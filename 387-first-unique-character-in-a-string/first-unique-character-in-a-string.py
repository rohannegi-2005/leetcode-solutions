class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        
        for i in range(n):
            s1 = s[0:i] + s[i+1:n]
            if s[i] not in s1:
                return i

        return -1
