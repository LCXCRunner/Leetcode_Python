class Solution:
    def isUgly(self, n: int) -> bool:
        while n % 2 == 0 and n > 0:
            n //= 2
        while n % 3 == 0 and n > 0:
            n //= 3
        while n % 5 == 0 and n > 0:
            n //= 5
        return True if n == 1 else False
        
solution : Solution = Solution()
print(solution.isUgly(6)) # True
print(solution.isUgly(1)) # True
print(solution.isUgly(14)) # False