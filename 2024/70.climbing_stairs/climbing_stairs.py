class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        else:
            n1 : int = 2
            n2 : int = 3
            nFinal : int = 3
            for i in range(3, n):
                nFinal = n1 + n2
                n1 = n2
                n2 = nFinal
            return nFinal

        #recursive approach is slow
        # def fibonacci(n1) -> int:
        #     if n1<= 0:
        #         return 0
        #     elif n1 == 1:
        #         return 0
        #     elif n1 == 2:
        #         return 1
        #     else:
        #         return fibonacci(n1-1)+fibonacci(n1-2)
        # return fibonacci(n+2)

solution : Solution = Solution()
print(solution.climbStairs(2))#2
print(solution.climbStairs(3))#3
print(solution.climbStairs(4))#5
print(solution.climbStairs(5))#8
print(solution.climbStairs(38))#63245986