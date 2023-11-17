class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)-1
        l=nums
        while(n):
            tmp=[]
            i=1
            while(i<len(l)):
                o=l[i]+l[i-1]
                if o>=10:
                    tmp.append(o%10)
                
                else:
                    tmp.append(o)
                i+=1
            l=tmp
            n-=1
        return l[0]
            