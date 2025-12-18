from collections import defaultdict

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        # build graph
        # defaultdict -> key = tuple(matrix cordinates) : value = list[neighboring cordinates that are not walls]
        # example: {(0,0): [(0,1),(1,0)], (0,1): [(0,0),(1,1)]}
        graph : defaultdict[tuple, list[tuple]] = defaultdict()
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "+":
                    continue
                else:
                    cordinate : tuple = (i,j)
                    graph[cordinate] = []
                    # check up
                    if i != 0:
                        if maze[i-1][j] == ".":
                            graph[cordinate].append((i-1, j))
                    # check right
                    if j != len(maze[i]) - 1:
                        if maze[i][j+1] == ".":
                            graph[cordinate].append((i, j+1))
                    # check down
                    if i != len(maze) - 1:
                        if maze[i+1][j] == ".":
                            graph[cordinate].append((i+1, j))
                    # check left
                    if j != 0:
                        if maze[i][j-1] == ".":
                            graph[cordinate].append((i, j-1))
        return graph

solution : Solution = Solution()
print(solution.nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2])) # 1
print(solution.nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0])) # 2
print(solution.nearestExit(maze = [[".","+"]], entrance = [0,0])) # -1