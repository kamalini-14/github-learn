class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=0
        c=0
        while(j<len(nums)):
            if nums[j] !=0:
                j+=1
                c=max(c,j-i)
            else:
                i=j+1
                j+=1
        return c