class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        w=s.split()
        for i in range(len(w)-1,0,-1):
            a+=w[i]
            a+=" "
        a+=w[0]
        return a