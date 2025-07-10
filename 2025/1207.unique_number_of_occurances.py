class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        result : bool = False
        dictionaryCounter : dict = {}
        for i in arr:
            if i in dictionaryCounter:
                count = dictionaryCounter.get(i)
                dictionaryCounter.update({i : count + 1})
            else:
                dictionaryCounter.update({i : 1})
        
        countValues : int = len(dictionaryCounter.values())
        if countValues == len(set(dictionaryCounter.values())):
            return True
        else:
            return result
            


# Given an array of integers arr, return true if the number of occurrences
# of each value in the array is unique or false otherwise.

solution : Solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3])) # T
print(solution.uniqueOccurrences([1,2])) # F
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # T