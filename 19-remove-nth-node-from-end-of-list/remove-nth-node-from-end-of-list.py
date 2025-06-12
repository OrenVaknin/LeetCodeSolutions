# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    #well use length func to know the length then use it to find the nth then connect prev to next:)
    def length(self, head):
        i=0
        while head:
            i+=1
            head=head.next
        return i
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        size=self.length(head)
        last=head
        prev=head
        if(n==size):
            return head.next
        if(n==1):
            l=1
            while l<size:
                before=last
                last=last.next
                l+=1
            before.next=None
            return head
        for _ in range(size-n-1):
            prev=prev.next
        nth=prev.next
        after=nth.next
        prev.next=after
        nth=None
        return head



        