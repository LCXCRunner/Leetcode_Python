from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack : deque = deque()
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            if stack[len(stack) - 1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

solution : Solution = Solution()
print(solution.removeDuplicates("abbaca")) # 'ca'
print(solution.removeDuplicates("azxxzy")) # 'ay'