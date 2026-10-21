# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = leftbv
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root==None:
            return 0
        from collections import deque
        q=deque([root])
        d=0
        while q:
            d+=1
            for i in range(len(q)):
                a=q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
        return d






