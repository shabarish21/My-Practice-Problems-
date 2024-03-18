class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Profit occurs if the previous day stock price is lesser than the current. So we set minimum price as compare it with all day prices. same is done for max_price also.
        min_price = prices[0] 
        max_profit = 0
        for i in prices[1:]:
            max_profit = max(max_profit,i-min_price)
            min_price = min(min_price,i)
        return(max_profit)