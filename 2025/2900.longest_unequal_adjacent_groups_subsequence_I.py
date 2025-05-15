class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n : int = len(words)
        prev : str = groups[0]
        result : list[str] = [words[0]]
        i : int = 1
        while i < n:
            while i < n and prev == groups[i]:
                i += 1
            if i < n:
                result.append(words[i])
                prev = groups[i]
            i += 1
        return result

solution : Solution = Solution()
print(solution.getLongestSubsequence(["e", "a", "b"], [0,0,1])) # ["e", "b"]
print(solution.getLongestSubsequence(["a", "b", "c", "d"], [1,0,1,1])) # ["a", "b", "c"]