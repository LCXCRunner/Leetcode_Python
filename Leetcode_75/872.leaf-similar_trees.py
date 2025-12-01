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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result : list = []
        def getLeaves(node : TreeNode, result : list) -> list:
            if node is None:
                return result
            # leetcode does not like the second half of the or function here, but it is needed to run locally. No idea why
            if node.left == None and node.right == None or node.right.val == None and node.left.val == None:
                result.append(node.val)
            else:
                result = getLeaves(node.left, result)
                result = getLeaves(node.right, result)
            return result 
        tree1Leaves : list = getLeaves(root1, result)
        result = []
        tree2Leaves : list = getLeaves(root2, result)
        if tree1Leaves == tree2Leaves:
            return True
        else:
            return False
                   

arr1 : list = [3,5,1,6,2,9,8,None,None,7,4]
arr2 : list = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))

solution : Solution = Solution()
print(solution.leafSimilar(tree1, tree2))