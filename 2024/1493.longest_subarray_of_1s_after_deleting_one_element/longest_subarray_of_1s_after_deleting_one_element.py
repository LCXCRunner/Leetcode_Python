class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        zeros = 0
        maxLength = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1 - zeros)

        if maxLength == n:
            return maxLength - 1
        return maxLength

solution : Solution = Solution()
print(solution.longestSubarray([1,1,0,1]))#3
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))#5
print(solution.longestSubarray([1,1,1]))#2 (you must delete one element)
print(solution.longestSubarray([1,0,0,0,1,0,1]))#2