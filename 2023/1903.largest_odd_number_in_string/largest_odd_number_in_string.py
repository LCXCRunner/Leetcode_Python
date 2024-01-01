class Solution: 
    def largestOddNumber(self, num : str) -> str:
        largest : int = -1
        for i in range(len(num)): 
            if int(num[i]) % 2 != 0:
                largest = i
            else:
                continue
        if largest == -1:
            return ""
        return str(num[slice(0,largest+1)])

solution : Solution = Solution()
print(solution.largestOddNumber("52"))#"5"
print(solution.largestOddNumber("4206"))#""
print(solution.largestOddNumber("35427"))#5"35427