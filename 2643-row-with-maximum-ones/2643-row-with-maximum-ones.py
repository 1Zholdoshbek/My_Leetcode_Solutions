class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count=0
        index=0
        for i in range(len(mat)):
            tmp=sum(mat[i])
            if count<tmp:
                count=tmp
                index=i 
        return [index,count]
        