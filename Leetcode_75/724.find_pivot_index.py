class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total : int = sum(nums)
        runningSum : int = 0
        for i in range(len(nums)):
            total -= nums[i]
            if total == runningSum:
                return i
            runningSum += nums[i]
        return -1

solution : Solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6])) # 3
print(solution.pivotIndex([1,2,3])) # -1
print(solution.pivotIndex([2,1,-1])) # 0
# print(solution.pivotIndex([1,2,3,6])) # 0