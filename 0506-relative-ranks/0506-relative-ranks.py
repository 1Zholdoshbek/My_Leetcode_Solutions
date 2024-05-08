class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tmp=sorted(score,reverse=True)
        d={}
        for i in range(len(score)):
            if i+1==1:
                d[tmp[i]]="Gold Medal"
            elif i+1==2:
                d[tmp[i]]="Silver Medal"
            elif i+1==3:
                d[tmp[i]]="Bronze Medal"
            else:
                d[tmp[i]]=str(i+1)
        return [d[i] for i in score]