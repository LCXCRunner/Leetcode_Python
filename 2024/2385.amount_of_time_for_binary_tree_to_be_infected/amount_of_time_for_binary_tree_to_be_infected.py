import BinarySearchTree
from BinarySearchTree import TreeNode
from collections import defaultdict
from collections import deque

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        #add the search tree to a graph
        #use the visited set to keep track of where you have been
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time
        

solution : Solution = Solution()
case1 : list = [1,5,3,None,4,10,6,9,2]
root : TreeNode = BinarySearchTree.insertLevelOrder(case1, 0, len(case1))
BinarySearchTree.levelOrder(root)
print()
print(solution.amountOfTime(root,3))