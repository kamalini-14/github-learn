class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        cc=[]
        f=[]
        for i in range(len(s)):
            if s[i]==c:
                cc.append(i)
            a.append(i)
            
        i=0
        while(i<len(a)):
            t=[]
            for j in cc:
                k=abs(a[i]-j)
                t.append(k)
            f.append(min(t))
            i+=1
        return f
