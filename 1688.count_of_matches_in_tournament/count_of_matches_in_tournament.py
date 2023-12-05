class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1 or n == 0:
            return 0
        result : int = 0
        #is even
        if n % 2 == 0:
            result = result + n / 2
            result = result + self.numberOfMatches(n/2)
        else:
            result = result + (n - 1) / 2
            result = result + self.numberOfMatches((n-1) / 2 + 1)
        return round(result)


solution : Solution = Solution()
print(solution.numberOfMatches(7))
print(solution.numberOfMatches(14))