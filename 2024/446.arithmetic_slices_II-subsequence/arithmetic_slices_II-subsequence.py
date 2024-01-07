class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        result : dict = {}
        spacer : int = 1
        i : int = 0
        j : int = i + 1
        n : int = len(nums)

        while spacer < n:
            while i < n: 
                while j < n:
                    print(nums[j])
                    j += spacer
                i += spacer
                j = i + spacer
            spacer += 1
            i = 0
            j = i + spacer

solution : Solution = Solution()
print(solution.numberOfArithmeticSlices([2,4,6,8,10]))#7
# print(solution.numberOfArithmeticSlices([7,7,7,7,7]))#16

# n = len(nums)
#         total_count = 0  
#         dp = [defaultdict(int) for _ in range(n)]

#         for i in range(1, n):
#             for j in range(i):
#                 diff = nums[i] - nums[j]
#                 dp[i][diff] += 1  
#                 if diff in dp[j]:
#                     dp[i][diff] += dp[j][diff]
#                     total_count += dp[j][diff]

#         return total_count