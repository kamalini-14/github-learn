class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=[]
        l=0
        c=0
        for r in range(len(s)):
            while(s[r] in a):
                a=a[1:]
                l+=1
            c=max(c,r-l+1)
            a.append(s[r])
        return c