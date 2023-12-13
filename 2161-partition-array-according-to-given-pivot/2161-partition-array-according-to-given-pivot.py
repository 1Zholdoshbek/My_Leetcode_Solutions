class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        mins=[]
        maxs=[]
        piv=[]
        for i in nums:
            if i<pivot:
                mins.append(i)
            elif i>pivot:
                maxs.append(i)
            else:
                piv.append(i)
        return mins+piv+maxs