# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        if root is None:
            return []
        q=deque([root])

        a=[]
        while q:
            ak=[]
            for i in range(len(q)):
                k=q.popleft()
                ak.append(k.val)
                if k.left:
                    q.append(k.left)

                if k.right:
                    q.append(k.right)
            a.append(ak)

        return a

