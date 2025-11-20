class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left : int = 0
        right : int = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k +=1
                left += 1
        
        return right - left + 1



solution : Solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10