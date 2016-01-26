char* longestCommonPrefix(char** strs, int strsSize) {
    int count = 0;
    char *q = "";
    if(strsSize == 0) return q;
    if(strsSize == 1) return strs[0];
    for(char *p = strs[0]; *p; p++){
        for(int i = 1; i < strsSize;i++){
            if(strs[i][count] == '\0' || strs[i][count] != *p){
                q = (char*)malloc(count+1);
                memcpy(q,strs[0],count);
                *(q+count) = '\0';
                return q;
            }
        }
        count ++;
    }
    q = (char*)malloc(count+1);
    memcpy(q,strs[0],count);
    *(q+count) = '\0';
    return q;
}
