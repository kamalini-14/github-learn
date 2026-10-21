# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root==None:
            return 0
        from collections import deque
        q=deque([root])
        d=0
        f=0
        while q:
            if f:
                break
            d+=1
            for i in range(len(q)):
                k=q.popleft()
                if k.left==None and k.right==None:
                    f=1
                    break
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
        return d