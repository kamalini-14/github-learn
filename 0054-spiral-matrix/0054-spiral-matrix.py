class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs=len(matrix)-1
        cs=len(matrix[0])-1
        l=0
        r=cs
        t=0
        b=rs
        ak=[]
        while(t<=b)and l<=r:
            for i in range(l,r+1):
                ak.append(matrix[l][i])
            t+=1
            for  i in range(t,b+1):
                ak.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    ak.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    ak.append(matrix[i][l])
            l+=1
        return ak