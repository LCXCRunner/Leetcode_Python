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
    def goodNodes(self, root: TreeNode) -> int:
        good : int = 0
        limit : int = root.val
        def helper(node : TreeNode, goodNodes : int, limit : int) -> int:
            if node is None or node.val == None:
                return goodNodes
            if node.val >= limit:
                limit = max(node.val, limit)
                goodNodes += 1
            goodNodes = helper(node.left, goodNodes, limit)
            goodNodes = helper(node.right, goodNodes, limit)
            return goodNodes
        return helper(root, good, limit)


arr1 : list = [3,1,4,3,None,1,5]
arr2 : list = [3,3,None,4,2]
arr3 : list = [1]

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))
tree3 : TreeNode = insertLevelOrder(arr3, 0, len(arr3))

solution : Solution = Solution()
print(solution.goodNodes(tree1))
print(solution.goodNodes(tree2))
print(solution.goodNodes(tree3))