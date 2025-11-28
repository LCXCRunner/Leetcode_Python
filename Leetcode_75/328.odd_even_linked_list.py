from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def appendToEnd(head : Optional[ListNode], node : Optional[ListNode]) -> Optional[ListNode]:
            # deal with empty list
            if head is None:
                node.next = None
                return node
            tail : ListNode = head
            # find the last node
            while tail.next is not None:
                tail = tail.next
            tail.next = node
            node.next = None
            return head

        prevNode : ListNode = ListNode(0)
        prevNode.next = head
        currNode : ListNode = prevNode.next
        oddIndexes : ListNode = None
        index : int = 0
        while currNode is not None:
            if index % 2 == 0:
                prevNode = currNode
                currNode = currNode.next
            else:
                prevNode.next = prevNode.next.next
                oddIndexes = appendToEnd(oddIndexes, currNode)
                currNode = prevNode.next
            index += 1
        prevNode.next = oddIndexes
        return head      

solution : Solution = Solution()
node : ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result : ListNode = solution.oddEvenList(node)
while result:
    print(result.val)
    result = result.next
print("-----")
node = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
result = solution.oddEvenList(node)
while result:
    print(result.val)
    result = result.next