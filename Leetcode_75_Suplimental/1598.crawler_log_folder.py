from collections import deque

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack : deque = deque()
        for i in logs:
            if i == "./":
                continue
            if i == "../" and len(stack) == 0:
                continue
            if i == "../":
                stack.pop()
            else:
                stack.append(1)
        return len(stack)

solution : Solution = Solution()
print(solution.minOperations(["d1/","d2/","../","d21/","./"])) #2
print(solution.minOperations(["d1/","d2/","./","d3/","../","d31/"])) #3
print(solution.minOperations(["d1/","../","../","../"])) #0