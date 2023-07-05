class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        poss = [0]
        for i in range(1, len(prices)):
            price = prices[i]
            if price < buy:
                buy = price
            elif price > buy:
                poss.append(price-buy)
                buy = prices[i]
        final = sum(poss)
        return final