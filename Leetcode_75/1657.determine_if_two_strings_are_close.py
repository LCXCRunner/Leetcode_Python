from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 : list = list(Counter(list(word1)).values())
        count2 : list = list(Counter(list(word2)).values())

        vals1 : list = list(Counter(list(word1)).keys())
        vals2 : list = list(Counter(list(word2)).keys())

        count1.sort()
        count2.sort()
        vals1.sort()
        vals2.sort()

        if count1 == count2 and vals1 == vals2:
            return True
        return False

solution : Solution = Solution()
print(solution.closeStrings("abc", "bca")) # true
print(solution.closeStrings("a" , "aa")) # false
print(solution.closeStrings("cabbba", "abbccc")) # true
print(solution.closeStrings("abbzccca" , "babzzczc")) # true
print(solution.closeStrings("uau", "ssx")) # false