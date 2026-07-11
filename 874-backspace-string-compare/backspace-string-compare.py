class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        lengthS = len(s)
        lengthT = len(t)

        for i in range(lengthS):
            if s[i] != "#":
                stackS.append(s[i])
            elif stackS:
                stackS.pop()

        # print(stackS)

        for i in range(lengthT):
            if t[i] != "#":
                stackT.append(t[i])
            elif stackT:
                stackT.pop()

        # print(stackT)

        if stackS == stackT:
            return True

        else:
            return False


        