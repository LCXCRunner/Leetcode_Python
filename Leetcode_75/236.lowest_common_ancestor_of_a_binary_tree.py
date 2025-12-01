from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.stackAncestorsP : deque = deque()
        self.hashSetQ : set = {}

        def findAncestorsP(node : TreeNode, target : TreeNode):
            if node is None:
                return
            self.stackAncestorsP.append(node.val)
            if node.val == target:
                return
            else:
                findAncestorsP(node.left, target)
                findAncestorsP(node.right, target)
                self.stackAncestorsP.pop()
        findAncestorsP(root, p)
        print(self.stackAncestorsP)


arr1 : list = [3,5,1,6,2,0,8,None,None,7,4]
arr2 : list = [3,5,1,6,2,0,8,None,None,7,4]
arr3 : list = [1,2]

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))
tree3 : TreeNode = insertLevelOrder(arr3, 0, len(arr3))

solution : Solution = Solution()
print(solution.lowestCommonAncestor(tree1, 5, 1)) # 3
print(solution.lowestCommonAncestor(tree2, 5,4)) # 5
print(solution.lowestCommonAncestor(tree3, 1,2)) # 1