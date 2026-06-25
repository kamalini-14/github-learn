class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        zc=0
        c=0
        for r in range(len(nums)):
            if nums[r]==0:
                zc+=1
            while(zc>k):
                if nums[l]==0:
                    zc-=1
                l+=1
            c=max(c,r-l+1)
        return c