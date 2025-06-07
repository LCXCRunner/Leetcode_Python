class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        startingPointer : int = 0
        endingPointer : int = len(nums) - 1
        while startingPointer <= endingPointer:
            if nums[startingPointer] != target:
                startingPointer += 1
            if nums[endingPointer] != target:
                endingPointer -= 1
            if nums[endingPointer] == target and nums[startingPointer] == target:
                return [startingPointer, endingPointer]
        return [-1,-1]

solution : Solution = Solution()
print(solution.searchRange([5,7,7,8,8,10],8)) # [3,4]
print(solution.searchRange([5,7,7,8,8,10],6)) # [-1,-1]