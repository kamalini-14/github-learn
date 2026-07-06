class Solution(object):
    def bt(self,x,y,sol,c,r,co):
        global t,zc,grid
        if x<0 or y<0 or x>=r or y>=co or self.grid[x][y]==-1 or sol[x][y]==1:
            return False
        if self.grid[x][y]==2:
            if c==self.zc+1: 
                self.t+=1
            return False
        sol[x][y]=1
        if self.bt(x,y+1,sol,c+1,r,co):
            return True
        if self.bt(x+1,y,sol,c+1,r,co):
            return True
        if self.bt(x,y-1,sol,c+1,r,co):
            return True
        if self.bt(x-1,y,sol,c+1,r,co):
            return True
        sol[x][y]=0
        return False
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.zc=0
        self.grid=grid
        r=len(grid)

        co=len(grid[0])
        for i in range(r):
            for j in range(co):
                if grid[i][j]==1:
                    dx=i
                    dy=j
                if grid[i][j]==0:
                    self.zc+=1
        sol=[[0]*co for i in range(r)]
        self.t=0
        self.bt(dx,dy,sol,0,r,co)
        print(self.t)
        return self.t