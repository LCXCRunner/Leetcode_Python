from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result : int = 0
        queue : deque = deque()
        while head is not None:
            queue.append(head.val)
            head = head.next
        while len(queue) > 0:
            result = max(queue.pop() + queue.popleft(), result)
        return result
    
solution : Solution = Solution()
node : ListNode = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
print(solution.pairSum(node)) # 6

node2 : ListNode = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
print(solution.pairSum(node2)) # 7

node3 : ListNode = ListNode(1, ListNode(100000))
print(solution.pairSum(node3)) # 100001