class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        o=capacity
        cnt=0
        for i,j in enumerate(plants):
            if o<j:
                cnt+=2*i
                o=capacity
            cnt+=1
            o-=j 
        return cnt
        
        