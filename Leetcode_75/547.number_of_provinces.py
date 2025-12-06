from collections import deque
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for cur, connected in enumerate(isConnected[city]):
                if connected and cur not in visited:
                    dfs(cur)
            
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces


solution : Solution = Solution()
print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) # 2
print(solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])) # 3
print(solution.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])) # 1