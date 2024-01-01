class Solution:
    def maxProductDifference(self, nums : list[int]) -> int:
        maxMax : int = max(nums)
        nums.remove(maxMax)
        miniMax : int = max(nums)
        nums.remove(miniMax)
        minMin : int = min(nums)
        nums.remove(minMin)
        miniMin : int = min(nums)

        print("maxMax: " + str(maxMax))
        print("miniMax: " + str(miniMax))
        print("minMin: " + str(minMin))
        print("miniMin: " + str(miniMin))

        return self.productDifference(maxMax,miniMax,minMin,miniMin)

    def productDifference(self, a : int, b : int, c : int, d : int) -> int:
        result : int = (a*b) - (c*d)
        return result

solution : Solution = Solution()
print(solution.maxProductDifference([7,6,2,5,4]))#34
print(solution.maxProductDifference([10,10,10,10]))#0
print(solution.maxProductDifference([2,9,5,9,1]))#79