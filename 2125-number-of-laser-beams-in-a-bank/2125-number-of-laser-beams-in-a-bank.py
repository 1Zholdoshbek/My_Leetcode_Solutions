class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l=[]
        for i in bank:
            if '1' in i:
                l.append(i)
        print(l)
        cnt=0
        for i in range(1,len(l),):
            tmp1=l[i-1].count('1')
            tmp2=l[i].count('1')
            cnt+=tmp1*tmp2
        return cnt
            
        