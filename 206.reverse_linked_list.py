from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        result : ListNode = None
        tempList : list = [head]
        tempNode : ListNode = head

        while tempNode.next != None:
            tempList.append(tempNode.next)
            tempNode = tempNode.next

        tempList.reverse()
        tempNode = tempList[0]
        result = tempNode

        for i in range(1,len(tempList)):
            tempNode.next = tempList[i]
            tempNode = tempNode.next
        tempNode.next = None

        return result

solution : Solution = Solution()
nodes : ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


tempNode = solution.reverseList(nodes) # 5 -> 4 -> 3 -> 2 -> 1
for i in range(5):
    print(tempNode.val)
    tempNode = tempNode.next
