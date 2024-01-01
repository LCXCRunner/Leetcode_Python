class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps : int = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                steps += 1
            else:
                num -= 1
                if num == 0:
                    steps += 1
                    break
                num = num / 2
                steps += 2
        return steps
    
solution : Solution = Solution()
print(solution.numberOfSteps(123))