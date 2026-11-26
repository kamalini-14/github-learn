class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        r=False
        a=9
        n-=10
        while n>=a:
            n-=a
            a-=1
            r = not r
        return not r