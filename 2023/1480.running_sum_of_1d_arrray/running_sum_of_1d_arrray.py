class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running : int = 0
        result : list = []
        for i in range(len(nums)):
            running += nums[i]
            result.append(running)
        return result
    
solution : Solution = Solution()
print(solution.runningSum([1,1,1,1,1,1,1]))