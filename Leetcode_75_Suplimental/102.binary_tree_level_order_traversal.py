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
    if i < n and arr[i] is not None:
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        self.tree : list[list] = []

        def collectLevels(node : TreeNode, level : int):
            if node is None or node.val is None:
                return
            
            # add another level if needed
            if len(self.tree) - 1 < level:
                self.tree.append([])
            
            # add node value to the proper level, due to depth first style recursion, it should stay in order
            self.tree[level].append(node.val)

            # drill down recursively
            collectLevels(node.left, level + 1)
            collectLevels(node.right, level + 1)
        collectLevels(root, 0)
        return self.tree
    
solution : Solution = Solution()

arr1 : list = [3,9,20,None,None,15,7]
arr2 : list = [1]
arr3 : list = []

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))
tree3 : TreeNode = insertLevelOrder(arr3, 0, len(arr3))

solution : Solution = Solution()
print(solution.levelOrder(tree1)) # [[3],[9,20],[15,7]]
print(solution.levelOrder(tree2)) # [[1]]
print(solution.levelOrder(tree3)) # []