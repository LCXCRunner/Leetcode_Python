class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                count += 1
        return count

tester : Solution = Solution()
print(tester.prefixCount(["apple", "app", "apricot", "banana", "apocalypse"], "ap")) # 4
print(tester.prefixCount(["pay","attention","practice","attend"], "at")) # 2