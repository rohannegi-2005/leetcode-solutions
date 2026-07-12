class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        place = 1

        while n > 0:
            digit = n % 10

            if digit != 0:
                ans.append(digit * place)

            place *= 10
            n //= 10

        return ans[::-1]