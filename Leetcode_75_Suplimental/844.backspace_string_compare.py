from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sResult : str = ""
        tResult : str = ""
        stackS : deque = deque(s)
        stackS.reverse()
        stackT : deque = deque(t)
        stackT.reverse()

        while len(stackS) != 0:
            if stackS[len(stackS) - 1] != "#":
                sResult += stackS.pop()
            else:
                stackS.pop()
                stackS.pop()
        print(sResult)

        while len(stackT) != 0:
            if stackT[len(stackT) - 1] == "#":
                tResult += stackT.pop()
            else:
                stackT.pop()
                stackT.pop()
        print(tResult)

        return tResult == sResult

solution : Solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c")) # true
print(solution.backspaceCompare("ab##", "c#d#")) # true
print(solution.backspaceCompare("a#c", "b")) # false