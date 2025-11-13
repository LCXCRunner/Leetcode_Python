from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        if head.next == None:
            return head
        else:
            pointer : ListNode = head.next
            tempNode : ListNode = None
        
        result : ListNode = head
        result.next = None

        while pointer != None:
            tempNode = pointer
            pointer = pointer.next
            tempNode.next = result
            result = tempNode

        return result

solution : Solution = Solution()
nodes : ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


tempNode = solution.reverseList(nodes) # 5 -> 4 -> 3 -> 2 -> 1
for i in range(5):
    print(tempNode.val)
    tempNode = tempNode.next
