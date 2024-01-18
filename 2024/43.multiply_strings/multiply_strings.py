class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 : int = 0
        n2 : int = 0
        power : int = len(num1) - 1

        # use ascii table value to convert to int. 
        for i in num1:
            n1 += 10**power * (ord(i) - 48)
            power -= 1

        power = len(num2) - 1
        for i in num2:
            n2 += 10**power * (ord(i) - 48)
            power -= 1

        return str(n1*n2)


solution : Solution = Solution()
print(solution.multiply("2","3"))#"6"
print(solution.multiply("123","456"))#"56088"