class Solution:
    def maxArea(self, height: list[int]) -> int:
        n : int = len(height)
        left : int = 0
        right : int = n - 1
        maxArea : int = 0

        while left < right:
            area : int = abs(right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea

solution : Solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(solution.maxArea([1,1])) # 1