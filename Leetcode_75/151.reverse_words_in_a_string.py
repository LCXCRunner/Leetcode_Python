class Solution:
    def reverseWords(self, s: str) -> str:
        array : list = s.split(" ")
        array = list(filter(None, array))
        array.reverse()
        return " ".join(array)

solution : Solution = Solution()
print(solution.reverseWords("the sky is blue")) # "blue is sky the"
print(solution.reverseWords("  hello world  ")) # "world hello"
print(solution.reverseWords("a good   example")) # "example good a"