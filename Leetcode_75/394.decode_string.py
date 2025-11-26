class Solution:
    def decodeString(self, s: str) -> str:
       print('hello world')

solution : Solution = Solution()
print(solution.decodeString("3[a]2[bc]")) # "aaabcbc"
print(solution.decodeString("3[a2[c]]")) # "accaccacc"
print(solution.decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"