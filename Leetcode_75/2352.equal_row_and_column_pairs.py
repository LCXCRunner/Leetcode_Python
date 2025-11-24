class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        transposed : list = [list(row) for row in zip(*grid)]
        count : int = 0
        
        for i in range(len(grid)):
            for j in range(len(transposed)):
                if grid[i] == transposed[j]:
                    count += 1
        return count

solution : Solution = Solution()
print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]])) # 1
print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # 3