class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], 0
        # profit = 
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
        print(buy, sell)
        poss.append(sell - buy)
        print(poss)
        final = max(poss)
        return final if final > 0 else 0
    # max를 0으로 두자
    