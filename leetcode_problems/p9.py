'''https://leetcode.com/problems/number-of-employees-who-met-the-target/'''
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in hours:
            if i>=target:
                c+=1
        return c