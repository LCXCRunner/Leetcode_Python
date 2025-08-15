import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n == 1:
        #     return True
        if n <= 0:
            return False
        # if n % 4 != 0:
        #     return False
        # while n > 4:
        #     n = n / 4
        #     if n % 4 != 0:
        #         return False
        # return True
        if (math.log(n) / math.log(4)) % 1 == 0:
            return True
        return False
        

solution : Solution = Solution()
print(solution.isPowerOfFour(16))  # True
print(solution.isPowerOfFour(5))   # False
print(solution.isPowerOfFour(1))   # True
print(solution.isPowerOfFour(256)) # True
print(solution.isPowerOfFour(257)) # False
print(solution.isPowerOfFour(0)) # False
print(solution.isPowerOfFour(8)) # False
print(solution.isPowerOfFour(-2147483648)) # False