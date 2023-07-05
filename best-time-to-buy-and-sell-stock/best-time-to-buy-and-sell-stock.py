class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], 0
        poss = [sell - buy]

        for i in range(1, len(prices)):
            price = prices[i]
            if price < buy:
                poss.append(sell - buy)
                buy = price
                sell = 0
            else:
                if price > sell:
                    sell = price
        poss.append(sell - buy)
        final = max(poss)
        return final if final > 0 else 0
    