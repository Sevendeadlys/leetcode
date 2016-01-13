/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4

that's the zigzag pattern the question asked! Be careful with nR=1 && nR=2
*/
char* convert(char* s, int numRows) {
   int len = strlen(s);
   if(numRows == 1) return s;
   char *result = (char *)malloc(len+1);
   int j = 0;

   for(int i = 0;i<numRows;i++){
       int step1 = (numRows-i-1)*2;
       int step2 = i*2;
       int pos = i;

       if(pos<len){
           result[j++] = s[pos];
       }
       while(1){
           pos += step1;
           if(pos >= len) break;
           if(step1) result[j++] = s[pos];
           pos += step2;
           if(pos >= len) break;
           if(step2) result[j++] = s[pos];
       }
   }
   result[j] = '\0';
   return result;
}
