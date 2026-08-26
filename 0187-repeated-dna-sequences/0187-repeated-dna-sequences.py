class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i=0
        j=10
        ch={}
        r=[]
        for j in range(10,len(s)+1):
            ak=s[i:j]
            if ak not in ch:
                ch[ak]=1
            else:
                if ch[ak]==1:
                    r.append(ak)
                    ch[ak]+=1
            i+=1
        return r