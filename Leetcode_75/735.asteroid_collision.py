class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        print('hello world')

solution : Solution = Solution()
print(solution.asteroidCollision([5,10,-5])) # [5,10]
print(solution.asteroidCollision([8,-8])) # []
print(solution.asteroidCollision([10,2,-5])) # [10]
print(solution.asteroidCollision([3,5,-6,2,-1,4])) # [-6,2,4]