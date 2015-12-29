/*
* the divisor cannot be zero
* the INT_MIN/-1 = INT_MAX
* Use the shift function to accelerate the substraction
*/
int divide(int dividend, int divisor) {
    int flag = 1;
    int ret = 0;
    long long a,b;

    if(divisor == 0) return INT_MAX;
    
    if(dividend == INT_MIN && divisor == -1) return INT_MAX;

    flag = ((dividend > 0)^(divisor < 0))?1:-1;

    a = labs(dividend);
    b = labs(divisor);

    long long temp;
    long long mul;
    while(a >= b)
    {
        temp = b;
        mul = 1;
        while(a >= (temp << 1))
        {
            temp = temp << 1;
            mul = mul << 1;
        }
        a -= temp;
        ret += mul;
    }
    return (flag > 0?ret:-ret);
}
