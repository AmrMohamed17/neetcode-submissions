class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, minimum = 0, max(prices)

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                max_profit = max(max_profit, price - minimum)

        
        return max_profit

        
        