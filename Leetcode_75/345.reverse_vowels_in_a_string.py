class Solution:
    def reverseVowels(self, s: str) -> str:
        result : list = list(s)
        left : int = 0
        right : int = len(s) - 1
        vowels : list = ["a", "i", "o", "u", "e", "A", "I", "O", "U", "E"]
        
        while left < right:
            if result[left] in vowels and result[right] in vowels:
                result[left] = s[right]
                result[right] = s[left]
                left += 1
                right -= 1 
                continue
            if result[left] not in vowels: 
                left += 1
            if result[right] not in vowels:
                right -= 1
        
        return "".join(result)

solution : Solution = Solution()
print(solution.reverseVowels("IceCreAm")) # AceCreIm
print(solution.reverseVowels("leetcode")) # leotcede