import heapq

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        monstersSlain : int = 0
        turnsToCity : list = []
        heapq.heapify(turnsToCity)
        turn : int = 0

        for i in range(len(dist)):
            turn = (dist[i] / speed[i])
            heapq.heappush(turnsToCity,turn)
        heapq.heappop(turnsToCity)
        monstersSlain += 1
        while(len(turnsToCity) !=0):
            if(monstersSlain < turnsToCity[0]):
                heapq.heappop(turnsToCity)
                monstersSlain += 1
            else:
                return monstersSlain
        return monstersSlain
    
solution : Solution = Solution()
print(solution.eliminateMaximum([3,5,7,4,5], [2,3,6,3,2]))
print(solution.eliminateMaximum([1,1,2,3], [1,1,1,1]))