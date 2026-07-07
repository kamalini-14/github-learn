class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pe=0
        c=0
        print(points)
        for i in range(len(points)):
            if i==0:
                pe=points[i][1]
                c+=1
            else:
                if points[i][0]>pe:
                    pe=points[i][1]
                    c+=1
        return c