class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = sorted(s)
        tSorted = sorted(t)
        if sSorted == tSorted:
            return True
        else:
            return False

solution : Solution = Solution()
print(solution.isAnagram("anagram","nagaram")) # True
print(solution.isAnagram("rat","car")) # False