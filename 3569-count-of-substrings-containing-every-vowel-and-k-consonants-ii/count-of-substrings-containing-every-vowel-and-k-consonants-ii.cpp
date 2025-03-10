class Solution {
public:

    bool vowel(char& c){
        if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')return true;
        return false;
    }

    long long countOfSubstrings(string word, int k) {
        map<char,long long> mp1;
        
        long long ccnt=0;
        long long answer=0;
        long long last=word.size();
        vector<long long> nextc(word.size());
        for(long long i=word.size()-1;i>=0;i--){
            nextc[i]=last;
            if(!vowel(word[i])){
                last=i;
            }
        }

        for(long long l=0,r=0;r<word.size();r++){
            if(vowel(word[r]))mp1[word[r]]++;
            else ccnt++;
            while(ccnt>k){
                if(vowel(word[l])){
                    mp1[word[l]]--;
                    if(mp1[word[l]]==0)mp1.erase(word[l]);
                }
                else ccnt--;
                l++;
            }
            while(ccnt==k && mp1.size()==5){
                answer+=(nextc[r]-r);
                if(vowel(word[l])){
                    mp1[word[l]]--;
                    if(mp1[word[l]]==0)mp1.erase(word[l]);
                }
                else ccnt--;
                l++;
            }
        }
        return answer;
    }
};