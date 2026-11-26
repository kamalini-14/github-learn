class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        a=[]
        for i in range(rowIndex+1):
            k=[0]*(i+1)
            k[0]=1
            k[i]=1
            a.append(k)
        for i in range(2,rowIndex+1):
            for j in range(i):
                if a[i][j]==0:
                    a[i][j]=a[i-1][j-1]+a[i-1][j]
        return a[rowIndex]