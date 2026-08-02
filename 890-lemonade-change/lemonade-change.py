class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bal = 0
        ten_bal = 0
        for amount in bills:
            if amount == 5:
                five_bal = five_bal + 1
            elif amount == 10:
                ten_bal = ten_bal + 1
                if five_bal > 0:
                    five_bal = five_bal - 1
                else:
                    return False
            else:
                if ten_bal > 0:
                    ten_bal = ten_bal - 1
                    if five_bal > 0:
                        five_bal = five_bal - 1
                    else:
                        return False

                else:
                    if five_bal > 2:
                        five_bal = five_bal - 3
                    else:
                        return False

        return True
            
        