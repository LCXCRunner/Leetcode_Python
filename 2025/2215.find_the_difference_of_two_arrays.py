class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        result : list[list[int]] = [[],[]]
        setNums1 : set = set(nums1)
        setNums2 : set = set(nums2)

        result[0] = list(setNums1 - setNums2)
        result[1] = list(setNums2 - setNums1)
        return result

solution : Solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))
print(solution.findDifference([1,2,3,3], [1,1,2,2]))