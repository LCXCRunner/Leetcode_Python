class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result : list[list[int]] = [[]]
        nums.sort()
        sortedNums : list = nums
        slotFound : bool = False

        for i in sortedNums:
            slotFound = False
            iteratorSlot : int = 0
            while slotFound == False:
                if i in result[iteratorSlot]:
                    if iteratorSlot == len(result) - 1:
                        result.append([])
                        iteratorSlot += 1
                        result[iteratorSlot].append(i)
                        slotFound = True
                    else:
                        iteratorSlot += 1
                        continue
                else:
                    result[iteratorSlot].append(i)
                    slotFound = True
        return result


solution : Solution = Solution()
print(solution.findMatrix([1,3,4,1,2,3,1]))#[[1,3,4,2],[1,3],[1]]
print(solution.findMatrix([1,2,3,4]))#[1,2,3,4]