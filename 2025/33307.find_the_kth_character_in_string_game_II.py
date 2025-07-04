class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
       word : list = ['a']
       tempWord : list = []
       for op in operations:
            if op == 0:
                word = word + word
            else:
                for i in range(len(word)):
                    tempWord = tempWord + [self.advanceCharacter(word[i])]
                word = word + tempWord
                tempWord = []
       return word[k-1]
    
    def advanceCharacter(self, c: str) -> str:
        # use ascii table - 97 is 'a', 98 is 'b', ..., 122 is 'z'
        if c == 'z':
            return chr(97)
        else:
            return chr(ord(c) + 1)
    
solution : Solution = Solution()
print(solution.kthCharacter(5, [0,0,0])) # Output: a
print(solution.kthCharacter(10, [0,1,0,1])) # Output: b
print(solution.kthCharacter(4, [1,1])) # Output: c
print(solution.kthCharacter(9499052, [0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1])) # Output: h