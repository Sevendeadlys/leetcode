bool isPalindrome(char* s) {
    int length = strlen(s);
    
    if(length == 0) return true;
    
    char *lo,*hi;
    lo = s;
    hi = s + length - 1;
    
    while(lo < hi){
        if(!isalnum(*lo)){
            lo ++;
        }
        else if(!isalnum(*hi)){
            hi --;
        }
        else{
            if(toupper(*lo) != toupper(*hi)) return false;
            lo ++;
            hi --;
        }
    }
    return true;
}