class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        a=0
        while(i<j):
            if height[i]<height[j]:
                k=height[i]*(j-i)
                i+=1
            elif height[j]<height[i]:
                k=height[j]*(j-i)
                j-=1
            else:
                k=height[i]*(j-i)
                i+=1
                j-=1
            print(a,k)
            a=max(a,k)
        return a