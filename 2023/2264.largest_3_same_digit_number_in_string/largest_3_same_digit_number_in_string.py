class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ""
        
        max3Digit : str = ""
        
        for i in range(2,len(num)):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                max3Digit = max(max3Digit,num[slice(i-2,i+1)])
        return max3Digit

solution : Solution = Solution()
print(solution.largestGoodInteger("6777133339"))#777
print(solution.largestGoodInteger("2300019"))#000
print(solution.largestGoodInteger("42352338"))#""