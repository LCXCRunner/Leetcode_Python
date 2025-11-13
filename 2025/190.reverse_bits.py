class Solution:
    def reverseBits(self, n: int) -> int:
        string : str = bin(n)
        string = string[2:]
        string = string.zfill(32)
        string = string[::-1].zfill(32)
        return int(string, 2)

solution : Solution = Solution()
print(solution.reverseBits(43261596)) # 964176192
print(solution.reverseBits(2147483644)) # 1073741822