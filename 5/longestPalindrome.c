/*
*travese the string,find all the palindrome, return the longest one
*/
char* longestPalindrome(char* s) {
    int length = strlen(s);
    if(length < 2) return s;

    int longest = 0;
    int a = 0,b = 0;
    for(int i = 0 ; i < length;){
        int lo = i;
        int hi = i;
        while(hi < length-1 && s[hi] == s[hi+1]) hi++;
        i = hi + 1;
        while(lo >0 && hi < length - 1 && s[lo-1]==s[hi+1]){
            lo --;
            hi ++;
        }
        if(longest < hi-lo+1){
            longest = hi - lo + 1;
            a = lo;
            b = hi + 1;
        }
    }
    if(b < length) s[b] = '\0';
    return s + a;
}
