class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies : int = max(candies)
        result : list = []
        for i in candies:
            if i + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result

solution : Solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3)) # [true,true,true,false,true] 
print(solution.kidsWithCandies([4,2,1,1,2], 1)) # [true,false,false,false,false]
print(solution.kidsWithCandies([12,1,12], 10)) # [true,false,true]