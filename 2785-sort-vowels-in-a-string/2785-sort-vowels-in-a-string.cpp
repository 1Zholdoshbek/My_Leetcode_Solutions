class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        p=[]
        l=['A','a','O','o','E','e','I','i','U','u']
        for index,char in enumerate(s):
            if char in l:
                v.append(char)
                p.append(index)
        v.sort()
        s=list(s)
        
        for index,char in zip(p,v):
            s[index]=char
            
            
        return ''.join(s)
            
            
        
        
        
            
                
            
           
           
           
           
            
        