class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        r=0
        for p in points:
            d=defaultdict(int)
            for q in points:
                di=(p[0]-q[0])**2 +(p[1]-q[1])**2
                d[di]+=1
            for c in d.values():
                r+=c*(c-1)
        return r