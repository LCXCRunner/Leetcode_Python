# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import ListNode

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tempNode : ListNode = head
        nodeList : ListNode = []
        middle : int = len(nodeList) // 2
        nodeList.append(tempNode)
        while tempNode.next != None:
            nodeList.append(tempNode.next)
            tempNode = tempNode.next
        middle : int = len(nodeList) // 2
        if(len(nodeList) == 1):
            return nodeList[0]
        else:
            return nodeList[middle]


solution : Solution = Solution()
head : ListNode = ListNode()
head.val = 1
second : ListNode = ListNode()
second.val = 2
head.next = second
third : ListNode = ListNode()
third.val = 3
second.next = third
# forth : ListNode = ListNode()
# forth.val = 4
# third.next = forth

print(solution.middleNode(head).val)