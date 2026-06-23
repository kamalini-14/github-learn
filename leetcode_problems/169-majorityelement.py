class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lc=0
        c=0
        l=set(nums)
        for i in l:
            if nums.count(i)>lc:
                lc=nums.count(i)
                c=i
        return c