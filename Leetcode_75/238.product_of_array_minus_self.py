class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result : list = []
        maxProduct : int = 1
        zeroProduct : int = 0

        if 0 in nums:
            if nums.count(0) == 1:
                for i in nums:
                    if i != 0 and zeroProduct != 0:
                        zeroProduct = zeroProduct * i
                    else:
                        zeroProduct = zeroProduct + i
            else:
                for i in nums:
                    if i != 0:
                        zeroProduct = zeroProduct * i

        for i in nums:
            maxProduct *= i

        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(zeroProduct)
                continue
            result.append(round(maxProduct * (nums[i]**(-1))))

        return result

solution : Solution = Solution()
print(solution.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(solution.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]