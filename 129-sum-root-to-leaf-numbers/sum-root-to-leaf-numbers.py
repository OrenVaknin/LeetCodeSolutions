# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    total = 0

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.preOrder(root,0)
        return self.total

    def preOrder(self,node,num):
        if not node:
             return
        num+=node.val
        if node.left is None and node.right is None:
            self.total+=num
            return
        self.preOrder(node.left,num*10)
        self.preOrder(node.right,num*10)