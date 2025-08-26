class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        result : int = 0
        maxDiagonal : float = 0
        for i in dimensions:
            diag : float = (i[0]**2 + i[1]**2)**(1/2)
            area : int = i[0] * i[1]
            if diag > maxDiagonal:
                maxDiagonal = diag
                result = area
            elif diag == maxDiagonal and result < area:
                result = area
        return result

solution : Solution = Solution()
print(solution.areaOfMaxDiagonal([[9,3],[8,6]])) # 48
print(solution.areaOfMaxDiagonal([[3,4],[4,3]]))# 12