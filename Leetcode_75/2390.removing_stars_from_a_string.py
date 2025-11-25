from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        result : deque = deque()
        stack : deque = deque(s)
        stack.reverse()
        
        while len(stack) != 0:
            if stack[len(stack)-1] != "*":
                result.append(stack.pop())
            else:
                result.pop()
                stack.pop()
        return "".join(result)

solution : Solution = Solution()
print(solution.removeStars("leet**cod*e")) # "lecoe"
print(solution.removeStars("erase*****")) # ""