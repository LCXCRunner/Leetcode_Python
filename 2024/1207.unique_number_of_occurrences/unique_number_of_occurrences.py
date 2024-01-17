class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurances : dict = {}
        #find out how many times each datapoint occurs
        for i in arr:
            if i in occurances:
                occurances.update({i : occurances.get(i) + 1})
            else:
                occurances.update({i:1})
        #count the number of occurances
        secondaryOccurances : dict = {}
        for i in occurances.values():
            if i in secondaryOccurances:
                secondaryOccurances.update({i : secondaryOccurances.get(i) + 1})
            else:
                secondaryOccurances.update({i:1})
        #if there are non 1's in the list, then the original datapoints did not have unique occurances
        for i in secondaryOccurances.values():
            if i != 1:
                return False
            else:
                continue
        return True

solution : Solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))#T
print(solution.uniqueOccurrences([1,2]))#F
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))#T