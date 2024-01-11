class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowels : int = 0
        vowels : dict = {"A", "I", "O", "U", "E"}
        left : int = 0
        right : int = k

        def countVowels(str : str) -> int:
            count : int = 0
            for i in str:
                if i.upper() in vowels:
                    count += 1
            return count

        while right <= len(s):
            maxVowels = max(maxVowels,countVowels(s[left:right]))
            left += 1
            right += 1
        return maxVowels

solution : Solution = Solution()
print(solution.maxVowels("abciiidef",3))#3
print(solution.maxVowels("aeiou",2))#2
print(solution.maxVowels("leetcode",3))#2
print(solution.maxVowels("d",1))#1