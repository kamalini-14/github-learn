# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root== None:
            return False
        v={}
        from collections import deque
        q=deque()
        q.append((root,root.val))
        while q:
            a,v=q.popleft()
            if a.left==None and a.right== None and v==targetSum:
                return True
            if a.left:
                q.append((a.left,v+a.left.val))
            if a.right:
                q.append((a.right,v+a.right.val))
        return False