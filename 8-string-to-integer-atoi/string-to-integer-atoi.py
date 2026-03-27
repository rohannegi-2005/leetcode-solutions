class Solution:
    def myAtoi(self, s: str) -> int:
        answer = ""
        flag = 0
        for i in s:
            if i == " " and len(answer) != 0:
                break
            if i != " ":
                if i == ".":
                    break
                if (i == "+" or i == "-") and flag == 1 :
                    break
                if (i == "+" or i == "-") and len(answer) != 0:
                    break
                if i.isdigit() or i == "+" or i == "-" :
                    answer = answer + i
                    if i == "+" or i == "-":
                        flag = 1
                else:
                    break
            
        print(answer)

        if answer == "+" or answer == "-":
            return 0
        
        if answer == "":
            return 0

        answer = int(answer)

        if answer > 2147483647 :
            return 2147483647

        if answer < -2147483648:
            return -2147483648



        return answer

        
    

        





        
        