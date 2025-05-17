class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # print(nums)

solution : Solution = Solution()
solution.sortColors([2,0,2,1,1,0]) # [0,0,1,1,2,2]
solution.sortColors([2,0,1]) # [0,1,2]