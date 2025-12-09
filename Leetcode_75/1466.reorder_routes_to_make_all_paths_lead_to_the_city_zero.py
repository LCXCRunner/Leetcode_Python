from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # construct the graph as well as the list of roads
        # graph:
        # key: city --- values: [roads, that, connect, to, city]
        #
        # roads:
        # a set with number pairs: {(0, 1), (4, 0), ...}
        roads : set = set()
        graph : defaultdict[list[int]] = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))

        def dfs(node):
            ans = 0
            # will iterate through each value of the graph. 
            for neighbor in graph[node]:
                if neighbor not in seen:
                    # basically looking to see if the road goes in the direction of the capital. 
                    if (node, neighbor) in roads: # This is the edge
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        seen = {0}
        return dfs(0)
    
solution : Solution = Solution()
print(solution.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])) # 3
print(solution.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]])) # 2
print(solution.minReorder(n = 3, connections = [[1,0],[2,0]])) # 0