class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)
        
        #find the compliment, if it is in the hashmap youre done. 
        #if not, add current nums index to the hashmap and move to the next
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
            
        #if not found, return []
        return []

#test case
print(Solution.twoSum((),[1,99,4,7],5))