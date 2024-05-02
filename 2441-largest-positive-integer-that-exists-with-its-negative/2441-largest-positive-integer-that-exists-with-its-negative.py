class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        tmp=[i for i in nums if i>0 ]
        tmp2=[i for i in nums if i<0 ]
        tmp=sorted(tmp,reverse=True)
        for i in tmp:
            if -i in tmp2:
                return i
        return -1
            
        