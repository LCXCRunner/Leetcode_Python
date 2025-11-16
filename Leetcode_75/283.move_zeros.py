class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros : list = []
        i : int = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                if len(nums) - i <= i:
                    break
            else:
                i += 1

        print(nums)

solution : Solution = Solution()
print(solution.moveZeroes([0,1,0,3,12])) # [1,3,12,0,0]
print(solution.moveZeroes([0,1,0,3,12])) # [1,3,12,0,0]