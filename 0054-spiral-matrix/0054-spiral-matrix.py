class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs=len(matrix)
        cs=len(matrix[0])
        l=0
        r=cs-1
        t=0
        b=rs-1
        ak=[]
        while(t<=b) and l<=r:
            for i in range(l,r+1):
                print(matrix[l][i])
                ak.append(matrix[l][i])
            t+=1
            for i in range(t,b+1):
                print(matrix[i][r])
                ak.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    print(matrix[b][i])
                    ak.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    print(matrix[i][l])
                    ak.append(matrix[i][l])
                l+=1
        return ak
        
