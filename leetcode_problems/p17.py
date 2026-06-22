'''https://leetcode.com/problems/intersection-of-two-arrays/'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in nums1:
            if i in nums2 and i not in a: 
                a.append(i)
        return a