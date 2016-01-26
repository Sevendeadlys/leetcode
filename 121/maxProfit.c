int maxProfit(int* prices, int pricesSize) {
    if(pricesSize < 2) return 0;
    int max = 0;
    int min = prices[0];
    
    for(int i = 1; i < pricesSize; i++){
        max = prices[i] - min > max ? prices[i] - min:max;
        if(prices[i] < min) min = prices[i];
    }
    return max;
}