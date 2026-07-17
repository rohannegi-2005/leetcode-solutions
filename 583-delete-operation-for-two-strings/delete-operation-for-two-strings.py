class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1] * m for _ in range(n)]

        def solve(i, j):
            if i == n or j == m:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] =  1 + solve(i+1, j+1)

            else:
                dp[i][j] = max(solve(i+1,j), solve(i, j+1))

            return dp[i][j]


        store = solve(0, 0)
        # return store
        add = n - store
        remove = m - store

        return (add + remove)




        


                                    

        