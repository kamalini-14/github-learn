class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        j=k
        c=0
        for _ in range(k):
            if blocks[_]=='W':
                c+=1
        m=c
        while(j<len(blocks)):
            if blocks[i]=='W':
                c-=1
            if blocks[j]=='W':
                c+=1
            m=min(c,m)
            i+=1
            j+=1
        return m