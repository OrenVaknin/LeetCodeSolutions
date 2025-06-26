# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        prev=ListNode(0)
        prev.next=head
        init=prev
        while head:
            if head.val==val:
                if head.next:
                    while head.next and head.next.val==val:
                        head=head.next
                    prev.next=head.next
                else: prev.next=None
            prev=head
            head=head.next
        return init.next
