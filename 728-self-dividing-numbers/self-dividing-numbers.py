class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left,right+1):
            number = i
            while i > 0 :
                num = i % 10
                if num == 0:
                    break
                elif number % num != 0 :
                    break
                else:
                    i = i // 10

            if i == 0:
                arr.append(number)

        return arr