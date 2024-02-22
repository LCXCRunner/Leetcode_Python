class Solution: 
    def findJudge(self, n : int, trust : list[list[int]]) -> int:
        initialPopulation : list[int] = []
        i : int = 1
        noTrust : list[int] = initialPopulation.copy()
        while i != n + 1: 
            noTrust.append(i)
            i += 1
        # Find out if there is anyone who trusts no one
        for i in trust:
            if i[0] in noTrust:
                noTrust.remove(i[0])
            else:
                continue
        if len(noTrust) == 0:
            return -1
        else:
            return (noTrust[0])
        
        # Find out if there is anyone that everyone trusts



solution : Solution = Solution()
print(solution.findJudge(2,[[1,2]]))#2
print(solution.findJudge(3,[[1,3],[2,3]]))#3
print(solution.findJudge(3,[[1,3],[2,3],[3,1]]))#-1
print(solution.findJudge(3,[[1,2],[2,3]]))#-1