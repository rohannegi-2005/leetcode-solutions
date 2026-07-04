from collections import deque
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        n = len(s)
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(dic)


        ans = ""

        for ch, count in sorted(dic.items(), key=lambda x:x[1], reverse=True):
            ans += ch * count

        return ans




        
            
