class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i=0
        j=k
        cs=sum(arr[:k])
        c=0
        if cs//k>=threshold:
            c+=1
        while(j<len(arr)):
            cs-=arr[i]
            cs+=arr[j]
            if (cs//k)>=threshold:
                c+=1
            i+=1
            j+=1
        return c