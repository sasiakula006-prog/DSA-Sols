# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        a = 0
        temp = head
        pre = head
        while temp:
            if a > n:
                pre = pre.next
            temp = temp.next
            a +=1
        if a ==n:
            head = head.next
        if a > n:
            if pre.next:
                pre.next = pre.next.next
            else:
                pre.next = None
            
        return head