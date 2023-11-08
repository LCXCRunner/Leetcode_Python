class Solution:
    def convert(self, s: str, numRows: int) -> str:
        oscillatorVariable : int = 0
        oscillatorFlag : bool = True
        result : list = [[]]
        finalResult : str = ""

        if(numRows == 1):
            return s

        #create 2D array
        for i in range(numRows - 1):
            result.append([])
        
        for i in range(len(s)):
            result[oscillatorVariable].append(s[i])
            if(i % (numRows-1) == 0):
                oscillatorFlag = not oscillatorFlag
            if(oscillatorFlag == False):
                oscillatorVariable += 1
            else:
                oscillatorVariable -= 1
        
        for i in range(numRows):
            result[i] = "".join(result[i])
        return "".join(result)
    
solution : Solution = Solution()
print(solution.convert("PAYPALISHIRING", 1))