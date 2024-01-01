class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        
        result : str = s[0]
        maxLen : int = 1
        forwardSub : str = ""
        backwardSub : str = ""

        for i in range(len(s)):
            for j in range(i + 1,len(s)):
                forwardSub = s[i:j+1]
                #slices the string backwards starting at the end and incrementing -1 each time
                backwardSub = forwardSub[::-1]
                if forwardSub == backwardSub:
                    if len(forwardSub) > maxLen:
                        result = forwardSub
                        maxLen = len(forwardSub)
                else:
                    continue
        return result

solution : Solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("ccc"))