class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tmp=''
        for i in s:
            tmp+=str((ord(i)-ord('a')+1))
        tmp2=0
        for _ in range(k):
            for i in tmp:
                tmp2+=int(i)
            tmp=str(tmp2)
            tmp2=0
        return int(tmp)
            
                    
            