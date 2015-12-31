bool isAnagram(char* s, char* t) {
    int buffer[128] = {0};
    int index = 0;

    if(!*s && !*t) return true;

    if(!*s || !*t) return false;

    char *p = s;
    char *q = t;
    for(; *p&&*q; p++,q++)
    {
        buffer[*p]++;
        buffer[*q]--;
    }
    if(*p || *q) return false;

    for(int index = 0; index < 128;index++)
    {
        if(buffer[index] != 0) return false;
    }
    return true;
}
