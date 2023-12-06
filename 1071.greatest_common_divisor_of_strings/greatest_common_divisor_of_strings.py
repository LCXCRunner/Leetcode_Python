class Solution: 
    def gcdOfStrings(self, str1 : str, str2 : str) -> str:
        result : str = str1
        biggerStr : str = str2
        count : int = 0
        if len(str1) > len(str2):
            result = str2
            biggerStr = str1
        
        while len(result) > 0:
            count = biggerStr.count(result)
            if count == 0:
                result = result[slice(1,len(result))]
                continue
            if len(biggerStr) / len(result) == count: #probably need to look at originals. 
                return result
            else:
                result = result[slice(1,len(result))]
        return result

solution : Solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))#"ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))#"AB"
print(solution.gcdOfStrings("LEET", "CODE"))#""
print(solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))#"TAUXX"
