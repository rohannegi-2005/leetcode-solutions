class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for money in accounts:
            max_sum = max(max_sum, sum(money))


        return max_sum
        
        