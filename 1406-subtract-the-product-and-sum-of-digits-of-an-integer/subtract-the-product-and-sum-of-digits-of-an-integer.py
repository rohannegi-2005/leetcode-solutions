class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            new_num = n % 10
            product = product * new_num
            sum = sum + new_num

            n = n // 10

        return product - sum


        