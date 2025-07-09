class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        quadruplets : list[list[int]] = []

        if len(nums) < 4:
            return quadruplets
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                left : int = j + 1
                right : int = len(nums) - 1

                while left < right: 
                    sum : int = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target: 
                        right -= 1
                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] in quadruplets:
                            left += 1
                            continue
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
        return quadruplets


solution : Solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2,2,2,2,2], 8)) # [[2,2,2,2]]
print(solution.fourSum([-2,-1,-1,1,1,2,2], 0)) # [[-2, -1, 1, 2], [-1, -1, 1, 1]]