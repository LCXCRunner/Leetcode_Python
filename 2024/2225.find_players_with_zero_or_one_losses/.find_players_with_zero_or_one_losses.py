class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        #list one is all players that have NOT lost a match. 
        #list two is all players that have lost exactly 1 match.
        winners : list[int] = []
        countedWinners : dict = {}
        losers : list[int] = []
        countedLosers : dict = {}
        n : int = len(matches)

        #strip away winners and losers
        for i in matches:
            winners.append(i[0])
            losers.append(i[1])

        for i in range(n):
            if countedWinners.get(winners[i]) is None:
                countedWinners.update({winners[i]:1})
            else:
                countedWinners.update({winners[i]:countedWinners.get(winners[i]) + 1})
            if countedLosers.get(losers[i]) is None:
                countedLosers.update({losers[i]:1})
            else:
                countedLosers.update({losers[i]:countedLosers.get(losers[i]) + 1})
        
        #find the ones that only lost once
        oneLoss : list[int] = []
        for i in countedLosers.keys():
            if countedLosers.get(i) == 1:
                oneLoss.append(i)
        oneLoss = sorted(oneLoss)

        #find the ones that have not lost
        noLoss : set = set()
        played : set = set()
        lost : set = set()
        for i in range(n):
            played.add(winners[i])
            played.add(losers[i])
            lost.add(losers[i])
        noLoss = played.difference(lost)
        noLoss = list(noLoss)
        noLoss = sorted(noLoss)
        
        return [list(noLoss), oneLoss]
        
solution : Solution = Solution()
print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))#[[1,2,10],[4,5,7,8]]
print(solution.findWinners([[2,3],[1,3],[5,4],[6,4]]))#[[1,2,5,6],[]]