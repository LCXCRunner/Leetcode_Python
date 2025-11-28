from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode : ListNode = None
        currNode : ListNode = head

        while currNode is not None:
            nextNode : ListNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        return prevNode

solution : Solution = Solution()
node : ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# node = solution.reverseList(node)
while node != None:
    print(node.val)
    node = node.next