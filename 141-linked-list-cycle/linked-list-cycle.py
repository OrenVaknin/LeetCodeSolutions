# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.next:
                if head.next.val=="deleted":
                    return True
            prev=head
            head=head.next
            prev.val="deleted"
        return False