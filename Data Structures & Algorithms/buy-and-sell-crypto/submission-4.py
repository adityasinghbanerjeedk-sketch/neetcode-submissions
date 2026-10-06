class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        L = 0
        minprice = prices[0]

        for R in range(len(prices)):

            if prices[R] < prices[L]:
                minprice = min(minprice, prices[R])
                L += 1
            else:
                maxprofit = max(maxprofit, prices[R] - minprice)

        return maxprofit
        