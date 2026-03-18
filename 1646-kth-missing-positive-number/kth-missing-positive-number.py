class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # array = []
        # last = max(arr)
        # for i in range(1,(last + 1),1):
        #     array.append(i)

        # print(array)

        # for i in arr:
        #     array.remove(i)

        # print(array)

        # try:
        #     return array[k-1]
        # except:
        #     return last + k - len(array)

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # missing numbers till index mid
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return k + low
        


        