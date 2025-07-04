class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
       # Calculate the length after each operation, we know it doubles each time regardless
        lengths = [1]
        for i in range(len(operations)):
            lengths.append(2**(i+1))
        # Work backwards to find the character at position k
        char = 'a'
        for i in range(len(operations)-1, -1, -1):
            if operations[i] == 0:
                if k > lengths[i]:
                    k -= lengths[i]
            else:
                if k > lengths[i]:
                    k -= lengths[i]
                    # Advance the character for this operation
                    char = self.advanceCharacter(char)
        return char
    
    def advanceCharacter(self, c: str) -> str:
        # use ascii table - 97 is 'a', 98 is 'b', ..., 122 is 'z'
        if c == 'z':
            return chr(97)
        else:
            return chr(ord(c) + 1)
    
solution : Solution = Solution()
# print(solution.kthCharacter(5, [0,0,0])) # Output: a
print(solution.kthCharacter(10, [0,1,0,1])) # Output: b
print(solution.kthCharacter(4, [1,1])) # Output: c
print(solution.kthCharacter(9499052, [0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1])) # Output: h