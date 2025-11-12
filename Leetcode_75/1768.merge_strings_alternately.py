class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result : str = ""
        n1 : int = len(word1)
        n2 : int = len(word2)
        i : int = 0

        while i < n1 and i < n2:
            result = result + word1[i]
            result = result + word2[i]
            i += 1

        if i < len(word2):
            result = result + word2[i:]
        else:
            result = result + word1[i:]

        return result

solution : Solution = Solution()
print(solution.mergeAlternately("abc", "pqr")) # "apbqcr"
print(solution.mergeAlternately("ab", "pqrs")) # "apbqrs"
print(solution.mergeAlternately("abcde", "pq")) # "apbqcde"