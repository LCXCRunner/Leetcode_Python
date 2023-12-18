class Solution:
    def reverseVowels(self, s : str) -> str:
        result = list(s)
        first : int = 0
        last : int = len(s) - 1
        temp : str = ""

        #walk them inward until they cross, swap as it finds vowel paris 
        while first <= last:
            if result[first].casefold() != 'a' and result[first].casefold() != 'e' and result[first].casefold() != 'i' and result[first].casefold() != 'o' and result[first].casefold() != 'u':
                first += 1 
                continue
            if result[last].casefold() != 'a' and result[last].casefold() != 'e' and result[last].casefold() != 'i' and result[last].casefold() != 'o' and result[last].casefold() != 'u':
                last -= 1
                continue
            result = list(result)
            temp = result[first]
            result[first] = result[last]
            result[last] = temp
            first += 1
            last -= 1
        return "".join(result)          
            

solution : Solution = Solution()
print(solution.reverseVowels("hEllo"))#holle
print(solution.reverseVowels("leEtcode"))#leotcede