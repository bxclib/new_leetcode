# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        temp = 0
        start = ListNode(0)
        now = start
        while l1 is not None or l2 is not None:
            now.next = ListNode(0)
            now = now.next
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            
            
            ans_temp = (x + y + temp)
            temp = ans_temp//10
            now.val = ans_temp%10

        if temp != 0:
            now.next = ListNode(temp)
        return start.next
