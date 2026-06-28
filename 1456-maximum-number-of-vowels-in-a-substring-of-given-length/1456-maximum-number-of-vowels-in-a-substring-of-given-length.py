class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        j=k
        v='AEIOUaeiou'
        m=0
        c=0
        for _ in range(k):
            if s[_] in v:
                c+=1
        m=c
        while(j<len(s)):
            if s[i] in v:
                c-=1
            if s[j] in v:
                c+=1
            m=max(c,m)
            i+=1
            j+=1
        return m