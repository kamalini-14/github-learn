class Solution:
    def maxLength(self, nums: List[int]) -> int:
        import math
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a=nums[i:j+1]
                #print(math.prod(a),(math.lcm(*a))*(math.gcd(*a)))
                if math.prod(a)==(math.lcm(*a))*(math.gcd(*a)):
                    print(a)
                    c=max(c,j-i+1)
                    print(c)
        return c