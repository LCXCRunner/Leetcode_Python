class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        result : float = sum(nums[:k])
        window : float = result
        for i in range(1,len(nums)-k+1):            
            window = window - nums[i-1] + nums[i+k-1]
            result = max(window, result)
        return result/k


solution : Solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3],4))#12.75
print(solution.findMaxAverage([5],1))#5.0
print(solution.findMaxAverage([-1],1))#-1.0