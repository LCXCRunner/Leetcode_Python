import copy

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        ordered : list[int] = copy.deepcopy(nums)
        setOrdered : set = set(ordered)
        ordered = list(setOrdered)
        ordered.sort()

        if len(ordered) < 3:
            return ordered[len(ordered) - 1]
        else:
            return ordered[-3]

solution : Solution = Solution()
print(solution.thirdMax([3,2,1])) # 1
print(solution.thirdMax([1,2])) # 2
print(solution.thirdMax([2,2,3,1])) # 1