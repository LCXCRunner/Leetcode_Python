class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # n : int = len(nums)

        # for i in range(n):
        #     for j in range(i,n):
        #         if nums[i] < nums[j]:
        #             for k in range(j,n):
        #                 if nums[j] < nums[k]:
        #                     return True
        # return False

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
print(solution.increasingTriplet([1,2,3,4,5])) # True
print(solution.increasingTriplet([5,4,3,2,1])) # False
print(solution.increasingTriplet([2,1,5,0,4,6])) # True