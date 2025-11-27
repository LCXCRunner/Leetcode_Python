class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total : int = 0
        diff : int = 0

        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i + 1] - timeSeries[i]
            total += min(diff, duration)
        total += duration

        return total

solution : Solution = Solution()
print(solution.findPoisonedDuration([1,4], 2)) # 4
print(solution.findPoisonedDuration([1,2], 2)) # 3