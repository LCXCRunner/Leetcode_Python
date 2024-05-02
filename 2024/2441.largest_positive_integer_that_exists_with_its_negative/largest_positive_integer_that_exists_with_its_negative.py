class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        while len(nums) > 0:
            if -1*max(nums) in nums:
                return max(nums)
            else:
                nums.remove(max(nums))
        return -1

solution : Solution = Solution()
print(solution.findMaxK([-1,2,-3,3]))#3
print(solution.findMaxK([-1,10,6,7,-7,1]))#7
print(solution.findMaxK([-10,8,6,7,-2,-3]))#-1
print(solution.findMaxK([14,33,40,-33,8,-24,-42,30,-18,-34]))#33