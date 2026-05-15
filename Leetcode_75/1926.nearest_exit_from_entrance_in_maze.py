from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows : int = len(maze)
        cols : int = len(maze[0])
        start_row : int = entrance[0]
        start_col : int = entrance[1]

        queue : deque = deque([(start_row, start_col, 0)])
        visited : set[tuple[int, int]] = {(start_row, start_col)}

        while queue:
            row, col, depth = queue.popleft()

            # Any border cell other than the entrance is an exit.
            if (row != start_row or col != start_col) and (
                row == 0 or col == 0 or row == rows - 1 or col == cols - 1
            ):
                return depth

            for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row : int = row + d_row
                next_col : int = col + d_col

                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                if maze[next_row][next_col] == "+":
                    continue
                if (next_row, next_col) in visited:
                    continue

                visited.add((next_row, next_col))
                queue.append((next_row, next_col, depth + 1))

        return -1
        
        


solution : Solution = Solution()
print(solution.nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2])) # 1
print()
print(solution.nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0])) # 2
print()
print(solution.nearestExit(maze = [[".","+"]], entrance = [0,0])) # -1
print()
print(solution.nearestExit(maze = [["+", "+", "+"], ["+", ".", "+"], ["+", ".", "+"]], entrance = [1,1])) # 1
print()
print(solution.nearestExit(
    maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]],
    entrance = [0,1]
)) # 12