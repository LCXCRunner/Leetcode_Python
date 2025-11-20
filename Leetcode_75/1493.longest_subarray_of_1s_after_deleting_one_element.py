class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left : int = 0
        right : int = 0
        k : int = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k +=1
                left += 1
        
        return right - left

solution : Solution = Solution()
print(solution.longestSubarray([1,1,0,1])) # 3
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
print(solution.longestSubarray([1,1,1])) # 2