# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        lvl=0
        if not root:
            return []
        def rec(node,lvl):
            if lvl>=len(ans):
                ans.append(node.val)
            if node.right:
                rec(node.right,lvl+1)
            if node.left:
                rec(node.left,lvl+1)

        rec(root,lvl)
        return ans
            