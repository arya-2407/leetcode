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
        #pre order traversal
        def dfs(root,maxVal):
            if not root:
                return 0
            
            #is it a good node?
            if root.val >= maxVal:
                res = 1
            else:
                res = 0
            maxVal = max(root.val,maxVal)
            res += dfs(root.left,maxVal)
            res += dfs(root.right,maxVal)
            return res
        
        if root:
            return dfs(root,root.val)
        else:
            return 0