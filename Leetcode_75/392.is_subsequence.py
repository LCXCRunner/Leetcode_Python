class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        sPointer : int = 0
        tPointer : int = 0

        while tPointer != len(t):
            if t[tPointer] == s[sPointer]:
                tPointer += 1
                sPointer += 1
            else:
                tPointer += 1
            if sPointer == len(s):
                return True
        return False


solution : Solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc")) # True
print(solution.isSubsequence("axc", "ahbgdc")) # False
print(solution.isSubsequence("", "ahbgdc")) # True
print(solution.isSubsequence("aza", "abzba")) # True
print(solution.isSubsequence("b", "abc")) # True