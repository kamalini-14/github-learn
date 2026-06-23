'''https://leetcode.com/problems/running-sum-of-1d-array/iven an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=[]
        c=0
        for i in nums:
            c+=i
            s.append(c)
        return s