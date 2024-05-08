class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranking : list = sorted(score, reverse=True)
        dRanking : dict = {}
        result : list[str] = []

        for i in range(len(ranking)):
            dRanking.update({ranking[i]:i+1})
        for i in score:
            if dRanking.get(i) == 1:
                result.append("Gold Medal")
            elif dRanking.get(i) == 2:
                result.append("Silver Medal")
            elif dRanking.get(i) == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(dRanking.get(i)))
        return result

solution : Solution = Solution()
print(solution.findRelativeRanks([5,4,3,2,1])) #["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(solution.findRelativeRanks([10,3,8,9,4])) #["Gold Medal","5","Bronze Medal","Silver Medal","4"]