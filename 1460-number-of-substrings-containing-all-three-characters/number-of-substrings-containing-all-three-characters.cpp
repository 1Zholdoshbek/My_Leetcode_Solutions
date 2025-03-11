class Solution {
public:
    int numberOfSubstrings(string s) 
    {
        int n = s.length();
        int i = 0, j = 0;
        int dchars = 0;
        int ans = 0;
        int counta = 0, countb = 0, countc = 0;
        
        while (j < n) 
        {
            while (j < n && dchars < 3) 
            {
                char ch = s[j];
                if (ch == 'a')
                {
                    if (counta == 0)
                    {
                        dchars++;
                    }
                    counta++;
                }
                else if (ch == 'b')
                {
                    if (countb == 0)
                    {
                        dchars++;
                    }
                    countb++;
                }
                else
                {
                    if (countc == 0)
                    {
                        dchars++;
                    }
                    countc++;
                }
                j++;
            }
            
            while (dchars == 3) 
            {
                char ch = s[i];
                if (ch == 'a')
                {
                    counta--;
                    if (counta == 0)
                    {
                        dchars--;
                    }
                }
                else if (ch == 'b')
                {
                    countb--;
                    if (countb == 0)
                    {
                        dchars--;
                    }     
                }
                else
                {
                    countc--;
                    if (countc == 0)
                    {
                        dchars--;
                    }
                }
                i++;
                
                ans += n - j + 1;
            }
        }
        return ans;
    }
};