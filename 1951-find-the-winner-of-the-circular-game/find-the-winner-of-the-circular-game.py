class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        
        # print(f"initial array:{arr}")

        i = 0
        while n > 1:
            i = (i + k - 1) % n
            arr.remove(arr[i])
            n = n - 1

        return arr.pop()

        





        