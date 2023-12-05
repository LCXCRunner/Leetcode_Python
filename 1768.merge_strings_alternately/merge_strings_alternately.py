class Solution: 
    def mergeAlternately(self, word1 : str, word2 : str) -> str:
        result : str = ""
        pullFromWord1 : bool = True
        list1 : list[str] = list(word1)
        list2 : list[str] = list(word2)

        #when there are char left in each list. 
        while len(list1) != 0 and len(list2) != 0:
            if pullFromWord1 == True:
                result = result + list1.pop(0)
                pullFromWord1 = not pullFromWord1
            else:
                result = result + list2.pop(0)
                pullFromWord1 = not pullFromWord1

        #when there is only char left in list1
        while len(list1) != 0:
            result = result + list1.pop(0)
        
        #when there is only char left in list2
        while len(list2) != 0:
            result = result + list2.pop(0)
        
        return result


solution : Solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))
print(solution.mergeAlternately("ab", "pqrs"))
print(solution.mergeAlternately("abcd", "pq"))