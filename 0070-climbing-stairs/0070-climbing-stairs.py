class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*n 
        if n>3:
            for i in range(n):
                if i<3:
                    dp[i]=i+1
                else:
                    dp[i]=dp[i-1]+dp[i-2]
        else:
            for i in range(n):
                dp[i]=i+1
        return dp[n-1]