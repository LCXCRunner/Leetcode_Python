class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result : list[int] = []
        tempStack : list[int] = []

        for i in asteroids:
            # need to consider the first being < 0
            if i >= 0:
                result.append(i)
            else: # is negative
                if not result and i < 0:
                    result.append(i)
                    continue
                elif max(result) < 0:
                    result.append(i)
                    continue
                while result:
                    while result[-1] < 0: # store all the negative moving asteroids
                        tempStack.append(result[-1])
                        result.pop()
                        if not result:
                            break
                    if abs(i) < result[-1]:
                        break # destroyed and not added
                    elif abs(i) > result[-1]:
                        result.pop()
                    elif abs(i) == result[-1]:
                        result.pop()
                        break
                    else: # destroyed all of the asteroids moving right
                        result.append(i)
                        break
                while tempStack: # put the negatives back in order
                    result.append(tempStack.pop())
        return result 

solution : Solution = Solution()
# print(solution.asteroidCollision([5,10,-5])) # [5,10]
# print(solution.asteroidCollision([8,-8])) # []
# print(solution.asteroidCollision([10,2,-5])) # [10]
# print(solution.asteroidCollision([-1, 10,5,-10])) # -1
# print(solution.asteroidCollision([-1, -2, 10,5,-10])) # -1, -2
# print(solution.asteroidCollision([-1, -2, -3, 5])) # -1, -2, -3, 5
print(solution.asteroidCollision([-2,-2,1,-2])) # -2,-2,-2