class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def operationNeeded(mid):
            operations = 0
            for num in nums:
                operations = operations + (num - 1) // mid

            return operations


        low = 1
        high = max(nums)

        while low < high :
            mid = (low + high) // 2

            if operationNeeded(mid) > maxOperations:
                low = mid + 1
            else:
                high = mid

        return low
        # print(operationNeeded(3))

        