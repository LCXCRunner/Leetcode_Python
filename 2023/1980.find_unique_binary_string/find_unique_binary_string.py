class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        possible_n : list = self.listOfAll(len(nums[0]))
        for i in range(len(possible_n)):
            if possible_n[i] not in nums:
                return possible_n[i]
                    
    def listOfAll(self,n : int) -> list:
        result : list = []
        formater : str = "0" + str(n) + "b"
        for i in range(2**n):
            result.append(format(i,formater))
        return result

solution : Solution = Solution()
print(solution.findDifferentBinaryString(["000","001","010"]))