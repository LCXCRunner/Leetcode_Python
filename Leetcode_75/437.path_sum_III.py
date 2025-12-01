from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def insertLevelOrder(arr : list, i : int, n : int) -> TreeNode:
    root = None
    # Base case for recursion 
    if i < n:
        root = TreeNode(arr[i]) 
 
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
 
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2, n)
    return root

# Print nodes at a current level
def currentLevel(root : TreeNode, level : int):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        currentLevel(root.left, level-1)
        currentLevel(root.right, level-1)

def height(node : TreeNode):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def levelOrder(root : TreeNode):
    h = height(root)
    for i in range(1, h+1):
        currentLevel(root, i)
    print()

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathArr : list = []
        def helper(node : TreeNode, path : list, targetSum : int) -> int:
            if node is None:
                return 0

            sums : int = 0
            path.append(node.val)

            runningSum : int = 0
            for i in reversed(path):
                if i is not None:
                    runningSum += i
                else:
                    break
                if runningSum == targetSum:
                    sums += 1
                else:
                    continue
            
            sums += helper(node.left, path, targetSum)
            sums += helper(node.right, path, targetSum)
            path.pop()
            return sums
        return helper(root, pathArr, targetSum)

arr1 : list = [10,5,-3,3,2,None,11,3,-2,None,1]
arr2 : list = [5,4,8,11,None,13,4,7,2,None,None,5,1]

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))

solution : Solution = Solution()
print(solution.pathSum(tree1, 8)) # 3
print(solution.pathSum(tree2, 22)) # 3