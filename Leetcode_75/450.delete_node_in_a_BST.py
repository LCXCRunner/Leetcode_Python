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

def levelOrder(root : TreeNode):
    h = height(root)
    for i in range(1, h+1):
        currentLevel(root, i)
    print()

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findNextNodeInNumericalSequence(currNode : TreeNode):
            # basically it moves one right and then all the way down the left after. 
            currNode = currNode.right
            while currNode is not None and currNode.left is not None:
                currNode = currNode.left
            return currNode
        
        if root is None:
            return None
        
        # find the node, if it exists
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right =  self.deleteNode(root.right, key)
        else:
            # node with either 0 or 1 child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # node with 2 children
            nextNode = findNextNodeInNumericalSequence(root)
            # assign the deleted node the value of the next in sequence.
            root.val = nextNode.val
            # delete the next in sequence
            root.right = self.deleteNode(root.right, root.val)
        return root
    
solution : Solution = Solution()

arr1 : list = [5,3,6,2,4,None,7]
arr2 : list = [5,3,6,2,4,None,7]

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))

solution : Solution = Solution()
levelOrder(solution.deleteNode(tree1, 3)) # [5,4,6,2,null,null,7]
levelOrder(solution.deleteNode(tree2, 0)) # [5,3,6,2,4,null,7]