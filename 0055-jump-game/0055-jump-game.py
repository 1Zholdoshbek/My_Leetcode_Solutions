class Solution:

    



    def canJump(self, A):

        m = 0

        for i in xrange(0,len(A)):

            if i<=m:

                m = max(A[i]+i,m)

                if m>=len(A)-1:

                    return True

        return False
 
 
        
        

        