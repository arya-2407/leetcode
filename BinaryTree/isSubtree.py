# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        #base case 1
        if not subRoot:
            return True
        #base case 2
        if not root:
            return False

        #check if current tree is same as subroot
        if self.isSameTree(root,subRoot):
            return True
        
        #check if either left or right are same as subroot.
        #OR because if either side is same, then it should be true 
        return (
            self.isSubtree(root.left,subRoot) or
            self.isSubtree(root.right,subRoot)
        )
                    
    
    #helper function
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        
        if (p and q) and (p.val==q.val):
            return (
                self.isSameTree(p.left,q.left) and
                self.isSameTree(p.right,q.right)
            )
        return False