# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #root is default lca
        lca = root

        #lca maybe changed if p and q are on the same side
        while lca:

            #p and q are on the right
            if p.val > lca.val and q.val > lca.val:
                lca=lca.right

            #p and q are on the left
            elif p.val < lca.val and q.val < lca.val:
                lca=lca.left
            
            #p and q are no longer on the same side
            else:
                return lca