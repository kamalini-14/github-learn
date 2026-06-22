'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        k=1
        while(i<len(nums)-1):
            j=i+1
            while (j<len(nums)-1) and (nums[j]==nums[i]):
                j+=1
            if j==len(nums)-1:
                if nums[j-1]==nums[j]:
                    k-=1
            nums[k]=nums[j]
            i=j
            k+=1
        return k
