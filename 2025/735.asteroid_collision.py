class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result : list[int] = []

        for i in asteroids:
            # need to consider the first being < 0
            while result and i < 0 < result[-1]:
                if -i > result[-1]:
                    result.pop()
                    continue
                elif -i == result[-1]:
                    result.pop()
                break
            else:
                result.append(i)
        return result 

solution : Solution = Solution()
print(solution.asteroidCollision([5,10,-5])) # [5,10]
print(solution.asteroidCollision([8,-8])) # []
print(solution.asteroidCollision([10,2,-5])) # [10]
print(solution.asteroidCollision([-1, 10,5,-10])) # -1
print(solution.asteroidCollision([-1, -2, 10,5,-10])) # -1, -2
print(solution.asteroidCollision([-1, -2, -3, 5])) # -1, -2, -3, 5
print(solution.asteroidCollision([-2,-2,1,-2])) # -2,-2,-2