class Solution:
    def increasingTriplet(self, nums : list[int]) -> bool:
        i = float('inf')
        j = float('inf')
        
        for k in nums:
            if k <= i:
                i = k
            elif k <= j:
                j = k
            elif k > j:
                return True
        return False

solution : Solution = Solution()
# print(solution.increasingTriplet([1,2,3,4,5]))#T
# print(solution.increasingTriplet([5,4,3,2,1]))#F
# print(solution.increasingTriplet([2,1,5,0,7,4,6]))#T
print(solution.increasingTriplet([20,100,10,12,5,13]))#T