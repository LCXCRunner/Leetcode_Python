# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val : int = val
        self.left : TreeNode = left
        self.right : TreeNode = right

# Function to insert nodes in level order 
def insertLevelOrder(arr : list, i : int, n : int):
    root = None
    # Base case for recursion 
    if i < n:
        root = TreeNode(arr[i]) 
 
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
 
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2, n)
         
    return root
 
# Functions to print tree nodes in: 
def inOrder(root : TreeNode):
    if root != None:
        inOrder(root.left) 
        print(root.val,end=" ") 
        inOrder(root.right)

def preOrder(root : TreeNode):
    if root:
        # First print the data of node
        print(root.val, end=" "),
        # Then recur on left child
        preOrder(root.left)
        # Finally recur on right child
        preOrder(root.right)

def postOrder(root : TreeNode):
    if root:
        # First recur on left child
        postOrder(root.left)
        # The recur on right child
        postOrder(root.right)
        # Now print the data of node
        print(root.val, end=" "),

def levelOrder(root : TreeNode):
    h = height(root)
    for i in range(1, h+1):
        currentLevel(root, i)
    print()
 
 
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

def leavesLeftToRight(node : TreeNode) -> list:
    if node is None:
        return
    def helper(currNode : TreeNode):
        if currNode is None:
            return
        if currNode.left == None and currNode.right == None or currNode.left.val == None and currNode.right.val == None:
            print(currNode.val)
            result.append(currNode.val)
            return
        else:
            helper(currNode.left) 
            helper(currNode.right)
    result : list = []
    helper(node)
    
if __name__ == '__main__':
    #             3
    #           /   \
    #         5       1
    #        / \     / \
    #       6   2   9   8
    #          / \
    #         7   4
    arr = [3,5,1,6,2,9,8,None,None,7,4]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n) 
    levelOrder(root)
    print()
    tester : list = leavesLeftToRight(root)
    print(tester)