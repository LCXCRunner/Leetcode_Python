class Solution: 
    def decodeString(self, s: str) -> str:
        stack : list[str] = []
        n : int = len(s)
        tempStr : str = ""
        tempNum : str = ""

        for i in range(n):
            if s[i] != "]":
                stack.append(s[i])
            else:
                while stack[-1] != "[":
                    tempStr = stack.pop() + tempStr
                stack.pop() # removes the [

                tempNum = ""
                while stack and stack[-1].isdigit():
                    tempNum = stack.pop() + tempNum
                
                tempStr = int(tempNum) * tempStr
                stack.append(tempStr)
                tempStr = ""
        return "".join(stack)

solution : Solution = Solution()
# print(solution.decodeString("3[a]2[bc]")) # aaabcbc
print(solution.decodeString("3[a2[c]]")) # accaccacc
print(solution.decodeString("2[abc]3[cd]ef")) # abcabccdcdcdef
print(solution.decodeString("100[leetcode]")) # leetcode x100