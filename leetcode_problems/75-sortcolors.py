class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            m=min(nums[i+1:])
            k=nums.index(m)
            nums[k],nums[i]=nums[i],nums[k]
        nums.sort()