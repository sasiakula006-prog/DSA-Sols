# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast =head
        while fast:
            fast = fast.next
            if fast:
                if fast == slow:
                    return True
                fast = fast.next 
                slow = slow.next
        return False
        