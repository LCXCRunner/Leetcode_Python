from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack : deque = deque()
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return list(stack)

solution : Solution = Solution()
print(solution.asteroidCollision([5,10,-5])) # [5,10]
print(solution.asteroidCollision([8,-8])) # []
print(solution.asteroidCollision([10,2,-5])) # [10]
print(solution.asteroidCollision([3,5,-6,2,-1,4])) # [-6,2,4]