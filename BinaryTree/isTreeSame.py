class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case
        if not p and not q:
            return True
        
        #both nodes exist and their vals are equal
        if (p and q) and (p.val==q.val):
            return (self.isSameTree(p.left,q.left) and
                    self.isSameTree(p.right,q.right))

        #this executes when (p or q dont exist while the other does not) or (both exist but their vals arent equal)
        return False