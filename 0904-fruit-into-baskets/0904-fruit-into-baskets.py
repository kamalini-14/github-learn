class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''a=[]
        l=0
        c=0
        for r in range(len(fruits)):
            a.append(fruits[r])
        while(len(set(a))>2):
            a=a[1:]
            l+=1
            c=max(c,r-l+1)
        return c'''
        from collections import defaultdict
        l=0
        d=defaultdict(int)
        mc=0
        for r in range(len(fruits)):
            d[fruits[r]]+=1
            while(len(d)>2):
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            mc=max(mc,r-l+1)
        return mc
                        
                   
    