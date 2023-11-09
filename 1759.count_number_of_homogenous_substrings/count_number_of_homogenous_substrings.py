class Solution:
    def countHomogenous(self, s: str) -> int:
        dictionary : dict = {}
        tally : int = 1

        if(len(s) == 1):
            return 1

        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                tally += 1
                if(i == len(s) - 2):
                    self.factorialAdd(dictionary,s[i],tally)
            else:
                self.factorialAdd(dictionary,s[i],tally)
                tally = 1
                if(i == len(s) - 2):
                    self.factorialAdd(dictionary,s[len(s)-1], 1)
        
        tally = 0
        for key in dictionary:
            tally += dictionary.get(key)
        
        return tally
        
    def factorialAdd(self,diction : dict, key : str, value : int):
        n : int = 1
        k : str = ""
        for i in range(value):
            k = k + key

        while(n <= value):
            if(diction.get(k) == None):
                diction.update({k : n})
                n = n + 1
                k = k[:len(k)-1]
                continue
            diction.update({key : n + diction[k]})
            k = k[:len(k)-1]
            n = n+1
    
solution : Solution = Solution()
print(solution.countHomogenous("oooorppppppppooooobbbjjjjcccccccccccceeeee"))