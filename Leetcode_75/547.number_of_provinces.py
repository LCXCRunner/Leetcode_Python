from collections import deque
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces : list[set] = [{0}]
        stack : deque = deque([0])  
        
        visited : set = set()
        visited.add(0)
        n : int = len(isConnected)
        while stack:
            node : int = stack.pop()
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    for province in provinces:
                        if node in province:
                            province.add(neighbor)
                            break
                    else:
                        provinces.append({neighbor})

        return len(provinces)


solution : Solution = Solution()
print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) # 2
print(solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])) # 3
print(solution.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])) # 1