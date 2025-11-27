from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant : deque = deque()
        dire : deque = deque()
        radiantCount : int = senate.count("R")
        direCount : int = senate.count("D")
        n : int = len(senate)

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while len(radiant) > 0 and len(dire) > 0:
            if radiant[0] < dire[0]:
                dire.popleft()
                radiant.append(n)
                radiant.popleft()
                n += 1
                direCount -= 1
            else:
                radiant.popleft()
                dire.append(n)
                n += 1
                dire.popleft()
                radiantCount -= 1
        
        if radiantCount <= 0:
            return "Dire"
        else:
            return "Radiant"
        
solution : Solution = Solution()
print(solution.predictPartyVictory("RD")) # "Radiant"
print(solution.predictPartyVictory("RDD")) # "Dire"
print(solution.predictPartyVictory("RRDDD")) # "Radiant"
print(solution.predictPartyVictory("RDR")) # "Radiant"