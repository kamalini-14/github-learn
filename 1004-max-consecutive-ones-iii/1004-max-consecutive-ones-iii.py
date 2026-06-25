class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zc=0
        m=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                zc+=1
            while(zc>k):
                if nums[l]==0:
                    zc-=1
                l+=1
            if zc<=k:
                m=max(m,r-l+1)
        return m