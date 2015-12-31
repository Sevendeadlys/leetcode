#define GET_NUM(x) (((x) - 'A') + 1)

int titleToNumber(char* s) {
    if(!*s) return 0;

    int len = strlen(s);
    int sum = 0;

    for(int index = len - 1; index > -1;index--)
    {
        sum =sum + GET_NUM(s[index]) * pow(26,len-index-1);
    }
    return sum;
}
