class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

solution : Solution = Solution()
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))#4
print(solution.lengthOfLIS([0,1,0,3,2,3]))#4
print(solution.lengthOfLIS([7,7,7,7,7,7,7]))#1