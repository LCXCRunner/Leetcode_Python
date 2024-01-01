class Solution:
    def numberOfWays(self, corridor: str) -> int:     
        numS : int = 0
        result : int = 1
        numP : int = 0
        mod : int = 10**9 + 7

        # everytime you encounter your second set of seats, the number of plants plus one will be the number of combos. 
        for i in corridor:
            if i == "S":
                numS += 1
            else:
                if numS == 2:
                    numP +=1
            if numS == 3:
                #result must multiply out as you go because of possible branching combos
                result = result*(numP + 1) % mod
                numS = 1
                numP = 0
        # edge case where you have odd or no seats
        if numS !=2:
            return 0
        
        return result

solution : Solution = Solution()
print(solution.numberOfWays("SSPPSPS"))#3
print(solution.numberOfWays("PPSPSP"))#1
print(solution.numberOfWays("SS"))#1
print(solution.numberOfWays("P"))#0
print(solution.numberOfWays("SPSPPSSPSSSS"))#6
print(solution.numberOfWays("SPPSSSSPPS"))#1
print(solution.numberOfWays("SPPSPSSPSSSPSPPSPPS"))#12