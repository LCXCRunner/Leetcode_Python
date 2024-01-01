class Solution: 
    def reverseWords(self, s : str) -> str:
        result : list = s.split()
        result.reverse()
        result = " ".join(result)
        return result

solution : Solution = Solution()
print(solution.reverseWords("the sky is blue"))
print(solution.reverseWords("  the  sky is blue  "))