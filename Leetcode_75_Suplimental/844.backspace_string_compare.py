from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)

solution : Solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c")) # true
print(solution.backspaceCompare("ab##", "c#d#")) # true
print(solution.backspaceCompare("a#c", "b")) # false