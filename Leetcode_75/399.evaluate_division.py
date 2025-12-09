from collections import defaultdict
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph : defaultdict[list[tuple[str, float]]] = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(start: str, end: str, seen: set[str]) -> float:
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            for neighbor, value in graph[start]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    product = dfs(neighbor, end, seen)
                    if product != -1.0:
                        return value * product
            return -1.0

        results : list[float] = []
        for a, b in queries:
            results.append(dfs(a, b, {a}))
        return results
        

solution : Solution = Solution()
print(solution.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])) # [6.0,0.5,-1.0,1.0,-1.0]
print(solution.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])) # [3.75,0.4,5.0,0.2]
print(solution.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]])) # [0.5,2.0,-1.0,-1.0]