class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result : int = 0
        binN : str = bin(n)
        binN = binN[2:]
        add : bool = True

        for i in binN:
            exp : int = 2**(len(binN)) - 1
            binN = binN[1:]
            if i == "1":
                if add == True:
                    result += exp
                    add = not add
                else: 
                    result -= exp
                    add = not add
            else: 
                continue
        return result
        
    def op1(self, binary : list) -> list:
        if binary[len(binary) - 1] == "1":
            binary[len(binary) - 1] = "0"
        else:
            binary[len(binary) - 1] = "1"
        return binary
        
    def op2(self, binary : list ) -> list:
        for i in reversed(range(len(binary))):
            if i == 0:
                break
            if binary[i] == "1":
                binary[i-1] = self.bitFlip(binary[i-1])
                break
            else:
                continue
                
    def bitFlip(self, bit : str) -> str:
        if bit == "1":
            bit = "0"
        else:
            bit = "1"
        return bit
    

solution : Solution = Solution()
print(solution.minimumOneBitOperations(3))#2 : 11 : false
print(solution.minimumOneBitOperations(2))#3 : 10 : true
print(solution.minimumOneBitOperations(6))#4 : 110 : false
print(solution.minimumOneBitOperations(21))#25 : 10101 : false
print(solution.minimumOneBitOperations(29))#22 : 110 : false
print(solution.minimumOneBitOperations(31))#29 : 110 : false
print(solution.minimumOneBitOperations(15))#10 : 1111 : false
print(solution.minimumOneBitOperations(33))#62 : 100001 : false
print(solution.minimumOneBitOperations(38))#59 : 100110 : true
print(solution.minimumOneBitOperations(782365))#876521
