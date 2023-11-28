class Solution:
    def numberOfWays(self, corridor: str) -> int:
        subString : str = ""
        numChairs : int = 0
        combos : int = 0
        mod = 10**9 + 7

        numS : int  = corridor.count("S")
        if(numS < 2):
            return 0
        if(numS == 2):
            return 1
        
        i : int = 0
        while(numChairs != 2):
            if(corridor[i] == "S"):
                numChairs += 1
                i += 1
            if(numChairs == 2):
                subString = corridor[i:]
                combos += 1
            if(corridor[i] == "P"):
                i += 1
                continue
            
        combos = self.helper(subString, 0)
        return combos % mod

    def helper(self, subStr : str, com : int) -> int:
        subString : str = ""
        numChairs : int = 0
        combos : int = 0
        preSequencialP : int = 0
        mod = 10**9 + 7

        if len(subStr) == 0:
            return 0

        for i in range(len(subStr)):
            if(subStr[i] == "S"):
                numChairs += 1
            if(subStr[i] == "P" and numChairs == 0):
                # if preSequencialP == 0:
                #     preSequencialP += 1
                preSequencialP += 1
                continue
            if(numChairs == 2):
                combos += 1
                subString = subStr[i+1:]
                combos = combos + preSequencialP
                combos = (combos + self.helper(subString, combos)) % mod
                break

        return combos % mod

solution : Solution = Solution()
print(solution.numberOfWays("SSPPSPS"))#3
print(solution.numberOfWays("PPSPSP"))#1
print(solution.numberOfWays("SS"))#1
print(solution.numberOfWays("P"))#0
print(solution.numberOfWays("SPSPPSSPSSSS"))#6
print(solution.numberOfWays("SPPSSSSPPS"))#1