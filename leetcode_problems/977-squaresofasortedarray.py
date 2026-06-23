class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            if i <0:
                j=(i*-1)
                a.append(j*j)
            else:
                a.append(i*i)
        a.sort()
        return a