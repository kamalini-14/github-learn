class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        a=[]
        if k==0:
            return [0]*len(code)
        elif k<0:
            k=k*-1
            j=len(code)-k-1
            i=len(code)-1
            s=sum(code[j:i])
            
            for ak in range(len(code)):
                s-=code[j]
                s+=code[i]
                print(i,j,s)
                i+=1
                j+=1
                a.append(s)
                if i==len(code):
                    i=0
                if j==len(code):
                    j=0
            

        else:
            i=0
            j=k
            s=sum(code[i:j])
            for ak in range(len(code)):
                s-=code[i]
                s+=code[j]
                print(s,code[i],code[j])
                i+=1
                j+=1
                a.append(s)
            
                if i==len(code):
                    i=0
                if j==len(code):
                    j=0
        return a

        