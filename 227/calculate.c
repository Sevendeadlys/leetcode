int calculate(char* s) {
    int num = 0;
    int num1 = 1;
    int result = 0;
    int pri = 0;

    int len = strlen(s);

    for(int index = 0;index < len;index++)
    {
        char c = s[index];

        if(c >= '0'&&c <= '9')
        {
            num = num * 10 + (c - '0');
        }
        else if(c == '+'){
            if(pri == 0){
                result += num;
            }
            else if(pri == 1){
                result -= num;
            }
            else if(pri == 2){
                num1 *= num;
                result += num1;
            }
            else if(pri == 3){
                if(num == 0) return 0;
                num1 /= num;
                result += num1;
            }
            num = 0;
            pri = 0;
            num1 = 1;
        }
        else if(c == '-'){
            if(pri == 0){
                result += num;
            }
            else if(pri == 1){
                result -= num;
            }
            else if(pri == 2){
                num1 *= num;
                result += num1;
            }
            else if(pri == 3){
                if(num == 0) return 0;
                num1 /= num;
                result += num1;
            }
            num = 0;
            pri = 1;
            num1 = 1;
        }
        else if(c == '*'){
            if(pri == 0){
                num1 = num;
            }
            else if(pri == 1){
                num1 = -num;
            }
            else if(pri == 2){
                num1 *= num;
            }
            else if(pri == 3){
                if(num == 0) return 0;
                num1 /= num;
            }
            pri = 2;
            num = 0;
        }
        else if(c == '/'){
            if(pri == 0){
                num1 = num;
            }
            else if(pri == 1){
                num1 = -num;
            }
            else if(pri == 2){
                num1 *= num;
            }
            else if(pri == 3){
                if(num == 0) return 0;
                num1 /= num;
            }

            pri = 3;
            num = 0;
        }
    }
    if(pri == 0){
        result += num;
    }
    else if(pri == 1){
        result -= num;
    }
    else if(pri == 2){
        num1 *= num;
        result += num1;
    }
    else if(pri == 3){
        if(num == 0) return 0;
        num1 /= num;
        result += num1;
    }
    return result;
}
