from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count : list = list(Counter(arr).values())
        unique : list = list(Counter(count).values())

        for i in unique:
            if i != 1:
                return False
        return True

solution : Solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3])) # true
print(solution.uniqueOccurrences([1,2])) # false
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true