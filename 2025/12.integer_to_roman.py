class Solution:
    def intToRoman(self, num: int) -> str:
        result : str = ""
        stringNum : list = list(str(num))
        length : int = len(stringNum)
        power : int = 10**(length - 1)
        for i in range(len(stringNum)):
            power = 10**(length - i - 1)
            result += self.romanHelper(stringNum[i], power)
        return result
    
    def romanHelper(self, num : str, power : int) -> str:
        # note: range is 1 <= x <= 3999
        if num == "0":
            return ""
        elif num == "4" or num == "9":
            # subtractive method
            if power == 100 and num == "4":
                return "CD"
            if power == 100 and num == "9":
                return "CM"
            if power == 10 and num == "4":
                return "XL"
            if power == 10 and num == "9":
                return "XC"
            if power == 1 and num == "4":
                return "IV"
            else: # power 1 and num = 9
                return "IX"
        elif num == "5":
            if power == 100:
                return "D"
            elif power == 10:
                return "L"
            else:
                return "V"
        else:
            result : str = ""
            if int(num) % 5 != 0 and int(num) > 5:
                result += self.romanHelper("5", power)
                num = int(num) % 5
            if power == 1000:
                result += "M" * int(num)
                return result
            elif power == 100:
                result += "C" * int(num)
                return result
            elif power == 10:
                result += "X" * int(num)
                return result
            else:
                result += "I" * int(num)
                return result
            
solution : Solution = Solution()
print(solution.intToRoman(900)) # CM
print(solution.intToRoman(45)) # IVV
print(solution.intToRoman(3749)) # MMMDCCXLIX
print(solution.intToRoman(58)) # LVIII
print(solution.intToRoman(1994)) # MCMXCIV