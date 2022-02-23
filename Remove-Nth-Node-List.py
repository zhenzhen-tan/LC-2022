# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(0)
        new_head.next = head
        fast = slow = new_head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return new_head.next

if __name__=="__main__":
    sol = Solution()
    sol.removeNthFromEnd([1, 2, 3, 4, 5], 2)
