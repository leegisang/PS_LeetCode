class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], 0
        poss = [0]

        for i in range(1, len(prices)):
            price = prices[i]
            if price < buy:
                # poss.append(sell - buy)
                buy = price
                # sell = 0
            elif price > buy:
                poss.append(price-buy)
                buy = prices[i]
                # if price > sell:
                #     sell = price
                #     poss.append(sell - buy)
        final = sum(poss)
        return final if final > 0 else 0