import BinarySearchTree
from BinarySearchTree import TreeNode

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leavesLeftToRight(node : TreeNode) -> list:
            if node is None:
                return
            def helper(currNode : TreeNode):
                if currNode is None:
                    return
                if currNode.left == None and currNode.right == None or currNode.left.val == None and currNode.right.val == None:
                    if currNode.val == None:
                        return
                    result.append(currNode.val)
                    return
                else:
                    helper(currNode.left) 
                    helper(currNode.right)
            result : list = []
            helper(node)
            return result

        l1 : list = leavesLeftToRight(root1)
        l2 : list = leavesLeftToRight(root2)
        print(l1)
        print(l2)

        if l1 == l2:
            return True
        else:
            return False

        
    
#testing
# case1_1 : list = [3,5,1,6,2,9,8,None,None,7,4]
# n1_1 : int = len(case1_1)
# case1_2 : list = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
# n1_2 : int = len(case1_2)

# case2_1 : list = [1,2,3]
# n2_1 : int = len(case2_1)
# case2_2 : list = [1,3,2]
# n2_2 : int = len(case2_2)

case3_1 : list = [4,2,6,1,3,5,7]
n3_1 : int = len(case3_1)
case3_2 : list = [4,2,6,None,3,5,7]
n3_2 : int = len(case3_2)

# unit1 : TreeNode = BinarySearchTree.insertLevelOrder(case1_1,0,n1_1)
# unit2 : TreeNode = BinarySearchTree.insertLevelOrder(case1_2,0,n1_2)
# BinarySearchTree.levelOrder(unit1)
# print()
# BinarySearchTree.levelOrder(unit2)
# print()
# solution1 : Solution = Solution()
# print(solution1.leafSimilar(unit1, unit2))

# print()

# unit3 : TreeNode = BinarySearchTree.insertLevelOrder(case2_1,0,n2_1)
# unit4 : TreeNode = BinarySearchTree.insertLevelOrder(case2_2,0,n2_2)
# BinarySearchTree.levelOrder(unit3)
# print()
# BinarySearchTree.levelOrder(unit4)
# print()
# solution2 : Solution = Solution()
# print(solution2.leafSimilar(unit3, unit4))

unit5 : TreeNode = BinarySearchTree.insertLevelOrder(case3_1,0,n3_1)
unit6 : TreeNode = BinarySearchTree.insertLevelOrder(case3_2,0,n3_2)
BinarySearchTree.levelOrder(unit5)
print()
BinarySearchTree.levelOrder(unit6)
print()
solution3 : Solution = Solution()
print(solution3.leafSimilar(unit5, unit6))