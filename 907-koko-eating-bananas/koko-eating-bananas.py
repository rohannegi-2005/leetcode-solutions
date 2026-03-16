class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        def calculate(k):
            total_hour = 0
            for pile in piles:
                hour = (pile + k - 1) // k
                total_hour = total_hour + hour

            return total_hour
                

        while low < high:
            mid = (low + high) // 2
            if calculate(mid) > h:
                low = mid + 1
            else:
                high = mid

        return low


            

            
        