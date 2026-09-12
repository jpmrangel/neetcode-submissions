class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bestSell = 0
        bestBuy = 101
        profit = 0
        for price in prices:
            profit = price - bestBuy

            if profit > maxProfit:
                maxProfit = profit
                bestSell = price

            if price < bestBuy:
                bestBuy = price
                bestSell = price
                
            

        return maxProfit