class Solution:
    def checkValidString(self, s: str) -> bool:

        low = 0
        high = 0

        for i in s:

            if i == "(":
                low = low + 1
                high = high + 1

            elif i == ")":
                low = low - 1
                high = high - 1

            else:
                low = low - 1
                high = high + 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0
            

            






        


        