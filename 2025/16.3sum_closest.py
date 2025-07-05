class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sum : int = nums[0] + nums[1] + nums[2]
        difference : int = abs(target - (nums[0] + nums[1] + nums[2]))
        smallestDifference : int = difference

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range (j + 1, len(nums)):
                    difference = abs(target - (nums[i] + nums[j] + nums[k]))
                    if difference < smallestDifference:
                        smallestDifference = difference
                        sum = nums[i] + nums[j] + nums[k]
        return sum

solution : Solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4],1)) # 2
print(solution.threeSumClosest([0,0,0], 1)) # 1
print(solution.threeSumClosest([-1,2,1,-4,-5,-9], -7)) # -7