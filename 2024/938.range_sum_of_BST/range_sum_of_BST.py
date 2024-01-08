from BinarySearchTree import TreeNode
import BinarySearchTree

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(TreeNode : TreeNode):
            if not TreeNode or TreeNode.val == None:
                return 0
            
            current_val = 0
            if low <= TreeNode.val <= high:
                current_val = TreeNode.val
            
            left_sum = dfs(TreeNode.left)
            right_sum = dfs(TreeNode.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)

solution : Solution = Solution()
testCase1 : list = [10,5,15,3,7,None,18]
n : int = len(testCase1)
root : TreeNode = BinarySearchTree.insertLevelOrder(testCase1,0,n)
BinarySearchTree.levelOrder(root)
print(solution.rangeSumBST(root, 7, 15))