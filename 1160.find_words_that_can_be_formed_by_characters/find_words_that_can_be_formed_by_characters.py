class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count : int = 0
        tempChars : str = chars
        for word in words: 
            tempChars = chars
            for i in range(len(word)):
                if word[i] in tempChars:
                    tempChars = tempChars.replace(word[i],"",1)
                    if i == len(word) - 1:
                        count += len(word)
                else:
                    break
        return count
        
        
tester : list = ["cat","bt","hat","tree"]
solution : Solution = Solution()
print(solution.countCharacters(tester, "atach"))
print(solution.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))