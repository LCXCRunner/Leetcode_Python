class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude : int = 0
        maxHeight : int = 0
        for i in gain:
            altitude += i
            maxHeight = max(maxHeight, altitude)
        return maxHeight

solution : Solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7])) # 1
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2])) # 0