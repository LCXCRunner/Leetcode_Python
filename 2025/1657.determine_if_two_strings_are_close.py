class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # check if you can just reorder using first method
        if sorted(word1) == sorted(word2):
            return True
        
        # check if you could swap occurances. 
        counter1 : dict = {}
        counter2 : dict = {}
        for i in range(len(word1)):
            if word1[i] not in counter1:
                counter1.update({word1[i] : 1})
            else:
                counter1.update({word1[i] : counter1.get(word1[i]) + 1})
            if word2[i] not in counter2:
                counter2.update({word2[i] : 1})
            else:
                counter2.update({word2[i] : counter2.get(word2[i]) + 1})
        if counter1.keys() == counter2.keys() and sorted(list(counter1.values())) == sorted(list(counter2.values())):
            return True
        else:
            return False

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, 
#   and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
solution : Solution = Solution()
print(solution.closeStrings("abc", "bca")) # T
print(solution.closeStrings("a", "aa")) # F
print(solution.closeStrings("cabbba", "abbccc")) # T
print(solution.closeStrings("abbzzca", "babzzcz")) # F
print(solution.closeStrings("abbzccca", "babzzczc")) # T