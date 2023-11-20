class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary : dict = {}
        for char in magazine:
            if char not in dictionary:
                dictionary.update({char:1})
            else:
                dictionary[char] += 1

        for target in ransomNote:
            if target not in dictionary:
                return False
            else:
                dictionary[target] -= 1
            if dictionary[target] < 0:
                return False
        return True
    
solution : Solution = Solution()
print(solution.canConstruct("aa", "aab"))