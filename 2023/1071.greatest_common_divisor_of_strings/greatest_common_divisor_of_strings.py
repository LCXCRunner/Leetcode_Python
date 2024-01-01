class Solution: 
    def gcdOfStrings(self, str1 : str, str2 : str) -> str:
        result : str = str1
        count1 : int = 0
        count2 : int = 0
        if len(str1) > len(str2):
            result = str2
        
        while len(result) > 0:
            count1 = str1.count(result)
            count2 = str2.count(result)
            if count1 == 0 or count2 == 0:
                result = result[slice(1,len(result))]
                continue
            if len(str1) / len(result) == count1 and len(str2) / len(result) == count2: #probably need to look at originals. 
                return result
            else:
                result = result[slice(1,len(result))]
        return result

solution : Solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))#"ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))#"AB"
print(solution.gcdOfStrings("LEET", "CODE"))#""
print(solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))#"TAUXX"
