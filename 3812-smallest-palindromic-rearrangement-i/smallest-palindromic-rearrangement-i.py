class Solution:
    def smallestPalindrome(self, s: str) -> str:

        dictionary = {}
        n = len(s)
        mid = n // 2
        print(mid)

        start = 0
        end = n - 1

        for i in s:

            if i in dictionary:
                dictionary[i] = dictionary[i] + 1
            else:
                dictionary[i] = 1


        dictionary = dict(sorted(dictionary.items()))


        ans = [""] * n

        for key in dictionary.keys():
            print(key)
            if dictionary[key] % 2 != 0:
                ans[mid] = key
                dictionary[key] = dictionary[key] - 1

            for count in range(dictionary[key] // 2):
                ans[start] = key
                ans[end] = key
                dictionary[key] = dictionary[key] - 2
                start = start + 1
                end = end - 1

        ans = "".join(ans)
        
        return ans

                


            



        
        