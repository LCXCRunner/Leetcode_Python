class Solution: 
    def maxWidthOfVerticalArea(self, points : list[list[int]]) -> int:
        #we really don't need the y cordinate of each point as the columns that we are looking at are infinitly tall. 
        xValues : list[int] = []
        maxWidth : int = 0
        #strip the x value of each pair, complexity of n
        for i in points:
            xValues.append(i[0])
        #sort in ascending order. Python sort uses Timsort and has time complexity of nlogn
        xValues.sort()
        #find the difference between each point in sorted xValues, complexity of n
        for i in range(len(xValues)-1):
            maxWidth = max(maxWidth, abs(xValues[i] - xValues[i+1]))
        return maxWidth

solution : Solution = Solution()
print(solution.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))#1
print(solution.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))#3