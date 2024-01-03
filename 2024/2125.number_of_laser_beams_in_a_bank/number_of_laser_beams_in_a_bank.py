class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        firstRow : int = 0
        result : int = 0
        firstValue : int = bank[0].count("1")

        if len(bank) == 1:
            return 0

        for nextRow in range(1,len(bank)):
            firstRow = nextRow - 1
            if bank[nextRow].count("1") == 0:
                continue
            else:
                result = result + firstValue * bank[nextRow].count("1")
                firstRow = nextRow
                firstValue = bank[firstRow].count("1")
        return result

solution : Solution = Solution()
print(solution.numberOfBeams(["011001","000000","010100","001000"]))#8
print(solution.numberOfBeams(["000","111","000"]))#0