class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        from collections import deque
        n=len(graph)
        t=(1<<n)-1
        q=deque()
        v=set()
        for i in range(n):
            q.append((i,1<<i))
        for i in range(n):
            v.add((i,1<<i))
        s=0
        while q:
            nn=len(q)
            for _ in range(len(q)):
                k,path=q.popleft()
                if path == t:
                    return s
                for i in graph[k]:
                    newj=path|(1<<i)
                    if (i,newj) not in v:
                        v.add((i,newj))
                        q.append((i,newj))
            s+=1