class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        
        # for i in range(n):
        #     s1 = s[0:i] + s[i+1:n]
        #     if s[i] not in s1:
        #         return i

        # return -1

        dictonary = {}
        for i in range(n):
            if s[i] in dictonary:
                dictonary[s[i]] = dictonary[s[i]] + 1
            else:
                dictonary[s[i]] = 1

        print(dictonary)

        answer = ''
        for word, count in (dictonary.items()):
            if count == 1:
                answer = word
                break

        for i in range(n):
            if s[i] == answer:
                return i

        return -1 

        
                

            

