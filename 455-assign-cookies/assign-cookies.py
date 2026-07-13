class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        g.sort()
        s.sort()

        print(f"g:{g}")
        print(f"s:{s}")

        n = len(g)
        m = len(s)

        x = 0
        y = 0
        
        while x < n and y < m:
            if g[x] <= s[y]:
                count = count + 1
                x = x + 1
                y = y + 1

            else:
                y = y + 1

        return count

            

        