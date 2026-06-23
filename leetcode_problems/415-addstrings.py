class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        k=0
        aj=0
        for i in range(len(num1)):
            a=int(num1[i])
            k=(k*10)+a
        for i in range(len(num2)):
            a=int(num2[i])
            aj=(aj*10)+a
        s=aj+k
        return str(s)