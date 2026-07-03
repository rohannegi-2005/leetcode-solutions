from collections import deque
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dictionary = {}
        j = 0
        n = len(fruits)
        max_count = 0
        
        for i in range(n):
            if fruits[i] in dictionary:
                dictionary[fruits[i]] = dictionary[fruits[i]] + 1
            else:
                dictionary[fruits[i]] = 1

            # print(dictionary)

            while len(dictionary) > 2:
                dictionary[fruits[j]] = dictionary[fruits[j]] - 1
                if dictionary[fruits[j]] == 0:
                    del dictionary[fruits[j]]
                j = j + 1

            max_count = max(max_count, i-j+1)
            

        return max_count







        
        
        