class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        array = []
        last = max(arr)
        for i in range(1,(last + 1),1):
            array.append(i)

        print(array)

        for i in arr:
            array.remove(i)

        print(array)

        try:
            return array[k-1]
        except:
            return last + k - len(array)
        


        