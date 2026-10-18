# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p==None and q==None:
            return True
        if p==None or  q==None:
            return False
        
        q1=deque([p])
        q2=deque([q])
        ak=[]
        aj=[]
        ak.append(p.val)
        aj.append(q.val)
        while q1 and q2:
            a=q1.popleft()
            k=q2.popleft()
            if a.left:
                q1.append(a.left)
                ak.append(a.left.val)
            else:
                ak.append(float('inf'))
            if k.left:
                q2.append(k.left)
                aj.append(k.left.val)
            else:
                aj.append(float('inf'))
            if a.right:
                q1.append(a.right)
                ak.append(a.right.val)
            else:
                ak.append(float('inf'))
            if k.right:
                q2.append(k.right)
                aj.append(k.right.val)
            else:
                aj.append(float('inf'))
        if ak==aj:
            return True
        else:
            return False