class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        targetPointer : int = 0
        testingPointer : int = 0

        if s == "" and t == "":
            return True
        if s == "":
            return True
        if len(t) == 0:
            return False

        while testingPointer != len(t):
            if t[testingPointer] == s[targetPointer]:
                testingPointer += 1
                targetPointer += 1
            else:
                testingPointer += 1
            if targetPointer == len(s):
                return True
        return False

solution : Solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))#T
print(solution.isSubsequence("axc", "ahbgdc"))#F
print(solution.isSubsequence("", "ahbgdc"))#T
print(solution.isSubsequence("a", "a"))#T