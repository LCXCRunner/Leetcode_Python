class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        result.append(words[i])
        result = list(set(result))
        return result

tester : Solution = Solution()
print(tester.stringMatching(["mass","as","hero","superhero"])) # ["as","hero"]
print(tester.stringMatching(["leetcode","et","code"])) # ["et","code"]
print(tester.stringMatching(["blue","green","bu"])) # []
print(tester.stringMatching(["leetcoder","leetcode","od","hamlet","am"])) # ["leetcode","od","am"]