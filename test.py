class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1 for _ in range(10)]

        for steps in range(0, n - 1):
            n = dp[:]
            dp[0] = n[4] + n[6]
            dp[1] = n[6] + n[8]
            dp[2] = n[7] + n[9]
            dp[3] = n[4] + n[8]
            dp[4] = n[3] + n[9] + n[0]
            dp[5] = 0
            dp[6] = n[1] + n[7] + n[0]
            dp[7] = n[2] + n[6]
            dp[8] = n[1] + n[3]
            dp[9] = n[2] + n[4]
            dp = [num % mod for num in dp]
        
        return sum(dp) % mod

solution : Solution = Solution()
print(solution.knightDialer(3))