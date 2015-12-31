#define ALLOC_SIZE 50
int calculate(char* s) {
    int* stack = (int*)malloc(ALLOC_SIZE*sizeof(int));
    int stack_size = ALLOC_SIZE;
    int len = strlen(s);
    int top = 0;
    int result = 0;
    int sign = 1;
    int num = 0;

    for(int index = 0; index < len;index ++){
        char c = s[index];

        if(c>='0' && c <= '9')
        {
            num = (int)(c-'0') + num*10;
        }
        else if(c == '+')
        {
            result += num * sign;
            num = 0;
            sign = 1;
        }
        else if(c == '-')
        {
            result += num * sign;
            num = 0;
            sign = -1;
        }
        else if(c == '(')
        {
            if((top + 1) >= stack_size){
                stack_size += ALLOC_SIZE;
                stack = (int*)realloc(stack,stack_size*sizeof(int));
            }
            stack[top++] = result;
            stack[top++] = sign;
            result = 0;
            sign = 1;
        }
        else if(c == ')')
        {
            result += num * sign;
            num = 0;
            result *= stack[--top];
            result += stack[--top];
            sign = 1;
        }

    }
    if(num != 0) result += num *sign;
    free(stack);
    return result;
}
