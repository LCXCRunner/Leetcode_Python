class Solution:
    def hammingWeight(self, n: int) -> int:
        result : int = bin(n).count("1")
        return result
solution : Solution = Solution()
print(solution.hammingWeight(0b11111111111111111111111111111101))