class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        # since nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) is the same as nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]) you only have to solve for the difference of one side
        result : int = 0
        count : dict = {}
        for i in range(len(nums)): 
            rev : int = nums[i] - int(self.reverseStr(str(nums[i])))
            if rev not in count:
                count[rev] = 1
            else:
                count[rev] += 1

        mod = (10**9 +7)
        for i in count:
            result += (count[i]*(count[i] - 1) // 2) % mod 
        #requested that it be returned modulo 10^9 +7
        return (result % mod)

    def reverseStr(self,s : str) -> str:
        string : str = ""
        for i in s:
            string = i + string
        return string

solution : Solution = Solution()
print(solution.countNicePairs([42,11,1,97]))
print(solution.countNicePairs([13,10,35,24,76]))