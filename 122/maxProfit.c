int maxProfit(int* prices, int pricesSize) {
    int sum = 0;

    for(int i = 1; i < pricesSize;i++){
        if(prices[i] > prices[i-1]){
            sum += prices[i] - prices[i-1];
        }
    }
    return sum;
}
