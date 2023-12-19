class Solution: 
    def productExecptSelf(self, nums : list[int]) -> list[int]:
        result : list[int] = []
        maxProduct : int = 1
        zeroProduct : int = 0

        #deal with the case of having either 1 or more zeros in the array
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

        #deals with an array with no zeros
        for i in nums:
            maxProduct = maxProduct * i
        
        #problem said no division to be used, it did not account for flipping the number using exponents. 
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(zeroProduct)
                continue
            result.append(round(maxProduct * (nums[i]**(-1))))
        return result 

solution : Solution = Solution()
print(solution.productExecptSelf([1,2,3,4]))
print(solution.productExecptSelf([-1,1,0,-3,3]))
print(solution.productExecptSelf([0,0]))
print(solution.productExecptSelf([0,4,0]))