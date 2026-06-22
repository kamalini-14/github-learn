''''https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/'''
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nc=0
        pc=0
        for i in nums:
            if i<0:
                nc+=1
            elif i>0:
                pc+=1
            else:
                continue
        return max(nc,pc)