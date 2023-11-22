class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        t=0
        i,j,k=0,0,0
        l=[]
        while i<len(s1) and j<len(s2) and k<len(s3):
            if s1[i]==s2[j] and s2[j]==s3[k]:
                i+=1
                j+=1
                k+=1
            else:
                break
        if i==0 or j==0 or k==0:
            return -1
        return (len(s1)-i)+(len(s2)-j)+(len(s3)-k)
            
        