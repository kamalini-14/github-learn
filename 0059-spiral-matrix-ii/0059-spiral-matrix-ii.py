class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rs=n
        cs=n
        a=[[0]*rs for i in range(cs)]
        cv=1
        t=0
        b=rs-1
        l=0
        r=cs-1
        while(t<=b and l<=r):
            for i in range(l,r+1):
                a[l][i]=cv
                cv+=1
            t+=1
            for i in range(t,b+1):
                a[i][r]=cv
                cv+=1
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    a[b][i]=cv
                    cv+=1
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    a[i][l]=cv
                    cv+=1
                l+=1
        return a

            