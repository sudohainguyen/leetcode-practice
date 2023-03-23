# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            slow = slow.next
        return slow
