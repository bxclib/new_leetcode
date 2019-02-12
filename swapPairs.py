# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return None
        if head.next is None:
            return head
        ans = head.next
        last_node = None
        while head is not None:
            if head.next is not None:
                if last_node is not None:
                    last_node.next = head.next
                temp = head.next.next
                head.next.next = head
                head.next = temp
            

                last_node = head
                head = head.next
            else:
                break

        return ans
