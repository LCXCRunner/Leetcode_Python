class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        rightSum : int = sum(nums)
        leftSum : int = 0

        for i in range(len(nums)):
            rightSum -= nums[i]
            if i == 0:
                pass
            else:
                leftSum += nums[i-1]
            if leftSum == rightSum:
                return i
        return -1

solution : Solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6])) # 3
print(solution.pivotIndex([1,2,3])) # -1
print(solution.pivotIndex([2,1,-1])) # 0
