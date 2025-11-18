import statistics

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        windowSum : float = sum(nums[0:k])
        average : float = round(windowSum / k, 5)

        for i in range(1, len( nums) - k + 1):
            windowSum = windowSum - nums[i - 1] + nums[i+k-1]
            average = max(average , round(windowSum / k, 5))

        return average

solution : Solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75000
print(solution.findMaxAverage([5], 1)) # 5.00000
print(solution.findMaxAverage([-1], 1)) # -1.00000
print(solution.findMaxAverage([0,1,1,3,3], 4)) # 2.00000