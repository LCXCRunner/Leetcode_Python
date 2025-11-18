class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, count = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxCount = 0

        for r in range(k):
            if s[r] in vowels:
                count += 1
        maxCount = max(maxCount, count)

        r = k
        while r < len(s):
            if s[r] in vowels:
                count += 1
            if s[l] in vowels:
                count -= 1
            maxCount = max(maxCount, count)
            l += 1
            r += 1 
        return maxCount


solution : Solution = Solution()
print(solution.maxVowels("abciiidef", 3)) # 3
print(solution.maxVowels("aeiou", 2)) # 2
print(solution.maxVowels("leetcode", 3)) # 2