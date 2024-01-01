class Solution:
    def kidsWithCandies(self, candies : list[int], extraCandies : int) -> list[bool]:
        result : list[bool] = []
        localMax : int  = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= localMax:
                result.append(True)
            else:
                result.append(False)
        return result

solution : Solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3],3))#TTTFT
print(solution.kidsWithCandies([4,2,1,1,2],1))#TFFFF
print(solution.kidsWithCandies([12,1,12],10))#TFT