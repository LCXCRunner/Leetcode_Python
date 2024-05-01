class Solution():
    def probabilityOfADiget(self,target : int, size : int) -> int:
        numOfPossibility : int = 10**size
        count = 0
        for i in range(numOfPossibility):
            if str(target) in str(i):
                count += 1
        return count

solution : Solution = Solution()
print(solution.probabilityOfADiget(4,4))