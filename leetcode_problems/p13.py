'''https://leetcode.com/problems/reverse-only-letters/'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while(i<j):
            if not(s[i].isalpha()):
                i+=1
                continue
            if not(s[j].isalpha()):
                j-=1
                continue
            else:
                t=s[i]
                s[i]=s[j]
                s[j]=t
                i+=1
                j-=1
        return "".join(s)