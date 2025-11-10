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
            if len(ans)==lvl:
                ans.append([])
            ans[lvl].append(node.val)
            level(node.left,lvl+1)
            level(node.right,lvl+1)

        level(root,0)
        return ans 
