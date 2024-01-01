class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        setOfNums = set(nums)
        for i in setOfNums:
            j = nums.count(i)
            if j == 1:
                return i
            
solution = Solution()
list =[1,1,2,2,3,4,4,5]
print(solution.singleNumber(list))