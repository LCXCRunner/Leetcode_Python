class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing spaces
        if not s:
            return 0

        sign : int = 1
        i : int = 0
        res : int = 0

        # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i]) # build the number by adding digits to the right

            # Handle overflow
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -2**31:
                return -2**31

            i += 1

        return sign * res

solution : Solution = Solution()
print(solution.myAtoi("42")) # 42
print(solution.myAtoi("   -42")) # -42
print(solution.myAtoi("4193 with words")) # 4193
print(solution.myAtoi("-00012")) # -12
print(solution.myAtoi("words and 987")) # 0
print(solution.myAtoi("-91283472332")) # -2147483648
print(solution.myAtoi("91283472332")) # 2147483647
print(solution.myAtoi("+-2")) # 0
print(solution.myAtoi("  -0012a42")) # -12
print(solution.myAtoi("1337c0d3")) # 1337
print(solution.myAtoi("+1")) # 1
print(solution.myAtoi("-+12")) # 0