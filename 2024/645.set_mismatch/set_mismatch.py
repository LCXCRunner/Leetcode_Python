class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        result : set = set()
        numsSorted : list[int] = nums.copy()
        numsSorted.sort()
        perfectSet : list[int] = []
        for i in range(len(numsSorted)):
            perfectSet.append(i+1)

        numsSet : set = set(nums)
        #find the duplicate number
        for i in range(len(numsSorted)-1):
            if numsSorted[i] == numsSorted[i+1]:
                result.add(numsSorted[i])
            if perfectSet[i] != numsSorted[i]:
                result.add(perfectSet[i])
            else:
                continue
        #find the missing number
        
        return list(result)

solution : Solution = Solution()
print(solution.findErrorNums([1,2,2,4]))#[2,3]
print(solution.findErrorNums([1,1]))#[1,2]
print(solution.findErrorNums([2,2]))#[1,2]
print(solution.findErrorNums([3,2,3,4,6,5]))#[3,1]