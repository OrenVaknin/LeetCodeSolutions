# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def inorder(node,goat):
            if node.val>=goat:
                self.ans+=1
                goat=node.val
            if node.right:
                inorder(node.right,goat)
            if node.left:
                inorder(node.left,goat)
        inorder(root,root.val)
        return self.ans