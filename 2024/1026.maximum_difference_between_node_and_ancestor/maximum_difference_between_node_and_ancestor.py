import BinarySearchTree
from BinarySearchTree import TreeNode

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        diffs : set = set()
        ancestors : set = set([root.val])

        def helper(ancest : set, currNode : TreeNode) -> set:
            tempAncest : set = set()
            tempAncest = ancest.copy()
            if currNode.val == None:
                return
            for i in tempAncest:
                diffs.add(abs(i - currNode.val))
            tempAncest.add(currNode.val)
            if currNode.left != None:
                helper(tempAncest, currNode.left)
            if currNode.right != None:
                helper(tempAncest, currNode.right)
            return
            

        if root.left != None:
            helper(ancestors, root.left)
        if root.right != None:
            helper(ancestors, root.right)

        return max(diffs)



# case1 : list = [8,3,10,1,6,None,14,None,None,4,7,13]
# root : TreeNode = BinarySearchTree.insertLevelOrder(case1, 0, len(case1))
# BinarySearchTree.levelOrder(root)
# solution : Solution = Solution()
# print(solution.maxAncestorDiff(root))

case2 : list = [1,None,2,None,0,3]
root2 : TreeNode = BinarySearchTree.insertLevelOrder(case2, 0, len(case2))
BinarySearchTree.levelOrder(root2)
solution2 : Solution = Solution()
print(solution2.maxAncestorDiff(root2))