# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans =[]
        def level(node,lvl):
            if not node:
                return
            while len(ans)<=lvl:
                ans.append([])
            ans[lvl].append(node.val)
            level(node.left,lvl+1)
            level(node.right,lvl+1)

        level(root,0)
        return ans 
        """
        ans = [[]]
        if root is None:
            return []
        self.ans = [[]]
        self.ans[0]=root.val
        self.level(root,0)
        return self.ans
    def level(self, root, lvl):
        while len(self.ans) <= lvl:
            self.ans. ([])
        if root.left or root.right:
            self.ans.append([])            
        if root.left:
            self.ans[lvl+1].append(root.left.val)
            return self.level(root.right,lvl+1)
        if root.right:
            self.ans[lvl+1].add(root.right.val)
            return self.level(root.left,lvl+1)"""