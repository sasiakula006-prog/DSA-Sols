# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        before = None
        current = head
        after = head.next
        while current:
            current.next = before
            before = current
            current = after
            if after:
                after = after.next
        head = before
        return head
        