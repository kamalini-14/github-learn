class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f=[0]*26
        for i in s1:
            f[ord(i)-97]+=1
        cs=s2[:len(s1)]
        fa=False
        j=len(s1)-1
        while(j<len(s2)):
            a=[0]*26
            for k in cs:
                a[ord(k)-97]+=1
            if f==a:
                return True
            if j==len(s2)-1:
                break
            cs=cs[1:]
            cs+=s2[j+1]
            j+=1

        return fa