class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left : int = 0
        right : int = len(nums) - 1
        nums.sort()
        result : int = 0

        while left < right:
            if k - nums[left] == nums[right]:
                nums.pop(right)
                nums.pop(left)
                result += 1
                right -= 2
            else:
                if k - nums[left] >= nums[right]:
                    left += 1
                else:
                    right -= 1
        return result

solution : Solution = Solution()
print(solution.maxOperations([1,2,3,4], 5))# 2
print(solution.maxOperations([3,1,3,4,3], 6))# 1
