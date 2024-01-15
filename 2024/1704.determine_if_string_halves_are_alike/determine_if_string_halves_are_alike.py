class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n : int = len(s)
        half : int = len(s)/2
        a : str = s[0:int(half)]
        b : str = s[int(half):n]
        aCount : int = 0
        bCount : int = 0
        vowels : list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in a:
            if i in vowels:
                aCount += 1
        for i in b:
            if i in vowels:
                bCount += 1
        
        if aCount == bCount:
            return True
        return False


solution : Solution = Solution()
print(solution.halvesAreAlike("book"))#T
print(solution.halvesAreAlike("leetcode"))#T
print(solution.halvesAreAlike("textbook"))#F