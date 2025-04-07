class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        # we can partition the array into two subsets with equal sum
        # only when the sum is even
        if total % 2: 
            return False
        # k is our target sum
        k = total // 2
        # subset sum problem -> solve it with DP
        dp = [True] + [False] * k
        # for each number
        for x in nums:
            # check all number from k to x
            # to check if adding x can achieve i
            for i in range(k, x - 1, -1): 
                dp[i] |= dp[i - x]
            # if dp[k] is achievable at a point, 
            # then we can return True
            if dp[k]: 
                return True
        return dp[k]
    
tester : Solution = Solution()
print(tester.canPartition([1,5,11,5])) # True
print(tester.canPartition([1,2,3,5])) # False
print(tester.canPartition([1,2,3,4,5])) # False
print(tester.canPartition([1,2,5])) # False
print(tester.canPartition([2,2,1,1])) # True