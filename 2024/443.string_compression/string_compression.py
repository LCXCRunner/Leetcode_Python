class Solution:
    def compress(self, chars: list[str]) -> int:
        compressedStr : str = ""
        result : int = 0
        frontPointer : int = 0
        backPointer : int = 0
        counterString : str = ""

        while backPointer != len(chars):
            if chars[frontPointer] == chars[backPointer]:
                backPointer += 1
                if backPointer == len(chars):
                    counterString = chars[frontPointer:backPointer]
                    if len(counterString) == 1:
                         compressedStr = compressedStr + str(chars[frontPointer])
                    else:
                        compressedStr = compressedStr + str(chars[frontPointer]) + str(len(counterString))
                continue
            else:
                counterString = chars[frontPointer:backPointer]
                if len(counterString) == 1:
                    compressedStr = compressedStr + str(chars[frontPointer])
                    
                else:
                    compressedStr = compressedStr + str(chars[frontPointer]) + str(len(counterString))
                frontPointer = backPointer
                backPointer += 1
                if backPointer == len(chars):
                    compressedStr = compressedStr + str(chars[frontPointer])
        result = len(compressedStr)
        for i in range(result):
            chars[i] = compressedStr[i:i+1]
        print(compressedStr)
        return result


solution : Solution = Solution()
print(solution.compress(["a","a","b","b","c","c","c"]))#6 with "a2b2c3"
print(solution.compress(["a"]))#1 with "a"
print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))#4 with "ab12"
print(solution.compress(["a","a","a","b","b","a","a"]))#6 with "a3b2a2"
print(solution.compress(["a","b","c"]))#3 with "abc"