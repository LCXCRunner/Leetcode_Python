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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest : int = 0

        # prev -> left is true and right is false
        def helper(node : TreeNode, count : int, prev : str) -> None:
            if node is None: 
                return count
            
            self.longest = max(self.longest, count)

            if node.left is not None:
                if prev != "left":
                    helper(node.left, count+1, 'left')
                else:
                    helper(node.left, 1, 'left')
            if node.right is not None:
                if prev != "right":
                    helper(node.right, count+1, 'right')
                else:
                    helper(node.right, 1, 'right')

        helper(root, 0, '')
        return self.longest
            
            

arr1 : list = [1,None,2,3,4,None,None,5,6,None,7,None,None,None,8] # i kinda think that this arr is wrong
arr2 : list = [1,1,1,None,1,None,None,1,1,None,1]
arr3 : list = [1]

tree1 : TreeNode = insertLevelOrder(arr1, 0, len(arr1))
tree2 : TreeNode = insertLevelOrder(arr2, 0, len(arr2))
tree3 : TreeNode = insertLevelOrder(arr3, 0, len(arr3))

solution : Solution = Solution()
print(solution.longestZigZag(tree1)) # 3
print(solution.longestZigZag(tree2)) # 4
print(solution.longestZigZag(tree3)) # 0