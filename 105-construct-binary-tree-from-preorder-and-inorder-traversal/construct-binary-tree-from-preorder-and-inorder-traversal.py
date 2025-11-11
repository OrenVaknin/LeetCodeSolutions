# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def inorderfind(val,inorder):
            for j in range(len(inorder)):
                if inorder[j] ==val:
                    return j
                j+=1
            return -1
        def split( preorder,inorder):
            if not preorder or not inorder:
                return None
            if len(preorder)==1:
                return TreeNode(preorder[0])
            rootVal=preorder[0]
            root=TreeNode(rootVal)
            inroot = inorderfind(rootVal,inorder)
            root.right=split(preorder[1+inroot:] , inorder[inroot+1:])    
            root.left=split(preorder[1:inroot+1] , inorder[:inroot])
            return root

        
        return split(preorder,inorder)



                     


