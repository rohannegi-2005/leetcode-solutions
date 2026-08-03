class Solution:
    def reorganizeString(self, s: str):

        n = len(s)

        dictionary = {}

        for letter in s:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1


        dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        print(dictionary)

        if dictionary[0][1] > (n+1)//2:
            return ""

        ans = [0] * n
        i = 0
        for x in dictionary:
            for _ in range(x[1]):
                ans[i] = x[0]
                i = i + 2
                if i >= n :
                    i = 1

        return "".join(ans)