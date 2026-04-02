class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, open, close, n , res):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if n > open:
                backtrack(curr + '(', open + 1, close, n, res)
            if open > close:
                backtrack(curr + ')', open, close + 1, n, res)

        def generate(n):
            res =[]
            backtrack("", 0, 0, n , res)
            return res


        result =  generate(n)

        return result

        