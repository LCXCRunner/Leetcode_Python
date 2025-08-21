class Solution:
    def isValid(self, s: str) -> bool:
        stack : list = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue

            peek : str = stack[len(stack) - 1]

            match char:
                case ")":
                    if peek == "(":
                        stack.pop()
                    else:
                        return False
                case "}":
                    if peek == "{":
                        stack.pop()
                    else:
                        return False
                case "]":
                    if peek == "[":
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(char)
        return not stack


solution : Solution = Solution()
print(solution.isValid("()")) # True
print(solution.isValid("()[]{}")) # True
print(solution.isValid("(]")) # False
print(solution.isValid("([])")) # True
print(solution.isValid("([)]")) # False
print(solution.isValid("[")) # False