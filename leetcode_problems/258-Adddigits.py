class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        if num<10:
            return num
        while(num>=10):
            s=0
            while(num>0):
                s+=num%10
                num=num//10
            if s>=10:
                num=s
        return s