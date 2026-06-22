'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        l=0
        r=1
        while(r<len(prices)):
            k=prices[r]-prices[l]
            if k>=0:
                a=max(a,k)
                r+=1
            else:
                l=r
                r+=1
        return a