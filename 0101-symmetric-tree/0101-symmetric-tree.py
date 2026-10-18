# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def issame(p,q):
            if p==None and q==None:
                return True
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False
            return (issame(p.left,q.right)) and (issame(p.right,q.left))
        return issame(root.left,root.right)