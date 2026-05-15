class Solution:
    def findMin(self, nums: list[int]) -> int:
        nums.sort()
        return nums[0]

solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2])) # 1
print(solution.findMin([4, 5, 6, 7, 0, 1, 2])) # 0
print(solution.findMin([11, 13, 15, 17])) # 11
