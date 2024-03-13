class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_1=0
        i=1
        for i in range(n+1):
            sum_1+=i
            sum_2=0
            for j in range(i,n+1):
                sum_2+=j
            if sum_1==sum_2:
                return i 
        return -1
            
        