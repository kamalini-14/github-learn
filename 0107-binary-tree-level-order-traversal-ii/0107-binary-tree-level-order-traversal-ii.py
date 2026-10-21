# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        if root==None:
            return []
        q=deque([root])
        a=[]
        while q:
            k=[]
            for i in range(len(q)):
                ak=q.popleft()
                k.append(ak.val)
                if ak.left:
                    q.append(ak.left)
                    #k.append(ak.left.val)
                if ak.right:
                    q.append(ak.right)
                    #k.append(ak.right.val)
            a.append(k)
        return a[::-1]