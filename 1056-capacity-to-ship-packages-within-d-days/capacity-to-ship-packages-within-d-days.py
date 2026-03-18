class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def day(capacity):
            total_weight = 0
            required_days = 1
            for weight in weights:
                if (total_weight + weight) <= capacity:
                    total_weight = total_weight + weight
                else:
                    required_days = required_days + 1
                    total_weight = weight

            return required_days

        max_capacity = 0
        for weight in weights:
            max_capacity = max_capacity + weight

        low = max(weights)
        high = max_capacity
        
        while low <= high:

            mid = (low + high) // 2

            if day(mid) <= days:
                high = mid - 1

            else:
                low = mid + 1

        return low 



        # print(days(3))
                 
        