class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sell_index = 0
        bought_index = 0
        # as soon as any index is lower than current bought_index,
        # record that as max_profit and move bought_index
        for i in range(len(prices)):
            if prices[i] < prices[bought_index]:
                max_profit = max(max_profit, prices[sell_index] - prices[bought_index])
                bought_index = i
                sell_index = i
            elif prices[i] > prices[sell_index]:
                sell_index = i
        max_profit = max(max_profit, prices[sell_index] - prices[bought_index])
        return max_profit
        