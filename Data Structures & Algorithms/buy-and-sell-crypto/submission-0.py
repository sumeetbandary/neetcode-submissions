class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_price = float('inf')
        
        for price in prices:
            if price < low_price:
                low_price = price
            else:
                max_profit = max(max_profit, price - low_price)
                
        return max_profit