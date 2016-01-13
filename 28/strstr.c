int strStr(char* haystack, char* needle) {
    char *q,*s;
    int count = 0;
    int len = strlen(haystack);
    int n = strlen(needle);

    if(!*needle) return 0;

    while(count < len && (len-count) >= n){
        q = needle;
        s = haystack + count;
        while(*q != '\0' && *s != '\0' && *q == *s){
            q++;
            s++;
        }
        if(*q == '\0' && *(s-1) == *(q-1))return count;

        count++;
    }
    return -1;
}
