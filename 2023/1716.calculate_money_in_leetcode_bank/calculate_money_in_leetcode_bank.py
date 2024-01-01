import math

class Solution:
    def totalMoney(self, n : int) -> int:
        result : int = 0
        count : int = -1
        for i in range (math.ceil(n/7)):
            if(count == n):
                    break
            for j in range(1,8):
                count += 1
                if(count == n):
                    break
                result = i + j + result
        return result

solution : Solution = Solution()
print(solution.totalMoney(4))#10
print(solution.totalMoney(10))#37
print(solution.totalMoney(20))#96
print(solution.totalMoney(0))#0