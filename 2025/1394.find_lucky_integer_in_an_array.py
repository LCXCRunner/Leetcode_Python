class Solution:
    def findLucky(self, arr: list[int]) -> int:
        largest : int = -1
        counts : dict[int, int] = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for key, value in counts.items():
            if key == value and key > largest:
                largest = key
        return largest

solution : Solution = Solution()
print(solution.findLucky([2,2,3,4])) # Output: 2
print(solution.findLucky([1,2,2,3,3,3])) # Output 3