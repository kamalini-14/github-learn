class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        k=len(needle)
        ak=haystack[0:k]
        i=0
        j=k
        while j<=n:
            if ak==needle:
                return i
            i+=1
            j+=1
            ak=haystack[i:j]
        return -1