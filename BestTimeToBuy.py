class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        maxprofit_price = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > maxprofit_price:
                maxprofit_price = price - min_price
        
        return maxprofit_price