import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return -1
    
        result : int = 0
        dictionary : dict = {}

        for i in nums:
            if i in dictionary:
                dictionary.update({i : dictionary.get(i) + 1})
            else:
                dictionary.update({i : 1})
            
        for i in dictionary:
            if dictionary.get(i) == 1:
                return -1
            else:
                result += math.ceil(dictionary.get(i) / 3)
        return result

solution : Solution = Solution()
print(solution.minOperations([2,3,3,2,2,4,2,3,4]))#4
print(solution.minOperations([2,1,2,2,3,3]))#-1
print(solution.minOperations([]))#-1
print(solution.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))#7
print(solution.minOperations([19,19,19,19,19,19,19,19,19,19,19,19,19]))#5