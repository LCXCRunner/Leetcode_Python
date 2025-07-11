class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count : int = 0
        transposed : list[list[int]] = []
        for row in range(len(grid)):
            transposed.append([])
            for col in range(len(grid[0])):
                transposed[row].append(grid[col][row])
        
        for i in grid:
            for j in transposed:
                if i == j:
                    count += 1
        
        return count

solution : Solution = Solution()
print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]])) # 1
print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # 3