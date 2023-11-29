class Solution:
    def numberOfWays(self, corridor: str) -> int:     
        sumArray : int = [-1]
        numS : int  = corridor.count("S")
        result : int = 0
        
        #special cases of only one S pair and no S
        if(numS < 2):
            return 0
        if(numS == 2):
            return 1       

        sumArray = self.recursiveHelper(sumArray, corridor, 1)
        if sumArray[0] == 0:
            return max(sumArray)
        else:
            return 1

    def recursiveHelper(self, array : list, subStr : str, counter : int) -> list:
        numOfS : int = 0
        numOfP : int = 0
        mod : int = 10**9 + 7 

        if len(subStr) == 0:
            return

        if subStr[0] == "S":
            for i in range(len(subStr)):
                if subStr[i] == "S":
                    numOfS += 1
                    if numOfS == 2:
                        array.append(0)
                        self.recursiveHelper(array, subStr[i+1:],counter)
                        break
        else:
            array[0] = 0
            for i in range(len(subStr)):
                if subStr[i] == "P":
                    numOfP += 1
                if subStr[i] == "S":
                    counter = counter*(numOfP + 1) % mod
                    array.append(counter)
                    self.recursiveHelper(array, subStr[i:],counter)
                    break
        return array

solution : Solution = Solution()
print(solution.numberOfWays("SSPPSPS"))#3
print(solution.numberOfWays("PPSPSP"))#1
print(solution.numberOfWays("SS"))#1
print(solution.numberOfWays("P"))#0
print(solution.numberOfWays("SPSPPSSPSSSS"))#6
print(solution.numberOfWays("SPPSSSSPPS"))#1
print(solution.numberOfWays("SPPSPSSPSSSPSPPSPPS"))#12

# subString : str = ""
#         numChairs : int = 0
#         combos : int = 0
#         mod = 10**9 + 7

#         numS : int  = corridor.count("S")
#         if(numS < 2):
#             return 0
#         if(numS == 2):
#             return 1
        
#         i : int = 0
#         while(numChairs != 2):
#             if(corridor[i] == "S"):
#                 numChairs += 1
#                 i += 1
#             if(numChairs == 2):
#                 subString = corridor[i:]
#                 combos += 1
#             if(corridor[i] == "P"):
#                 i += 1
#                 continue
            
#         combos = self.helper(subString, 0)
#         return combos % mod

#     def helper(self, subStr : str, com : int) -> int:
#         subString : str = ""
#         numChairs : int = 0
#         combos : int = 0
#         preSequencialP : int = 0
#         mod = 10**9 + 7

#         if len(subStr) == 0:
#             return 0

#         for i in range(len(subStr)):
#             if(subStr[i] == "S"):
#                 numChairs += 1
#             if(subStr[i] == "P" and numChairs == 0):
#                 # if preSequencialP == 0:
#                 #     preSequencialP += 1
#                 preSequencialP += 1
#                 continue
#             if(numChairs == 2):
#                 combos += 1
#                 subString = subStr[i+1:]
#                 combos = combos + preSequencialP
#                 combos = (combos + self.helper(subString, combos)) % mod
#                 break

#         return combos % mod