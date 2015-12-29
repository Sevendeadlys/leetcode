/*
*map the word and position
*traverse the string,update the position when meet the old word,
*update the max_num
*/
int lengthOfLongestSubstring(char* s) {
    int slen = strlen(s);
    int map[256];
    int max_num = 0;
    int m = 0;

    if(slen < 2) return slen;

    max_num = 1;
    map[s[0]] = 0;
    for(int i = 1; i < slen; ++i){
        if(map[s[i]] >= 0 ){
            m = map[s[i]]+1;
        }
        map[s[i]] = i;
        int longest = i - m + 1;
        if(max_num <= longest) max_num = longest;
    }

    return max_num;
}
