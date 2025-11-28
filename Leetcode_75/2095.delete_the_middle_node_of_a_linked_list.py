from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :return None
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return prev.next

solution : Solution = Solution()
node : ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
node = solution.deleteMiddle(node)
while node != None:
    print(node.val)
    node = node.next

print('-----')

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
node = solution.deleteMiddle(node)
while node != None:
    print(node.val)
    node = node.next

print('-----')

node = ListNode(1)
node = solution.deleteMiddle(node)
while node != None:
    print(node.val)
    node = node.next

print('-----')
node = ListNode(1, ListNode(2))
node = solution.deleteMiddle(node)
while node != None:
    print(node.val)
    node = node.next
