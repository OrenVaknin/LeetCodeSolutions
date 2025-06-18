# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        lower_ptr= ListNode(0)
        higher_ptr=ListNode(0)
        lower=lower_ptr
        higher=higher_ptr
        while head:
            if x>head.val:
                lower.next=head
                lower=lower.next
            else:

                higher.next=head
                higher=higher.next
            head=head.next
        higher.next=None
        lower.next=higher_ptr.next
        return lower_ptr.next