'''https://leetcode.com/problems/reverse-vowels-of-a-string/'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiou"
        i=0
        j=len(s)-1
        s=list(s)
        while(i<j):
            if s[i].lower() not in v:
                i+=1
                continue
            if s[j].lower() not in v:
                j-=1
                continue
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
