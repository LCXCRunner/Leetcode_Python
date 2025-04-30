class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count : int = 0
        for i in nums:
            convertString : str = str(i)
            if len(convertString) % 2 == 0:
                count += 1
        return count

solution : Solution = Solution()
print(solution.findNumbers([12,345,2,6,7896])) # 2
print(solution.findNumbers([555,901,482,1771])) # 1