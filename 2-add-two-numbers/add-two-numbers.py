# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length1= self.length(l1)
        length2= self.length(l2)
        if length1<length2:
            l1, l2=l2, l1
        flag=0
        starter= ListNode(0)
        starter.next=l1
        while l1!=None and l2!=None:
            l1.val=l1.val+l2.val+flag
            if l1.val>9:
                flag=1
                l1.val=l1.val%10
            else: flag=0
            prev = l1
            l1=l1.next
            l2=l2.next
        if(flag==1):
            while l1!=None and flag==1:
                l1.val+=flag
                if l1.val<=9:
                    flag=0
                l1.val=l1.val%10
                prev=l1
                l1=l1.next
            if flag==1:
                last= ListNode(1)
                prev.next=last
        return starter.next

