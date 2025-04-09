class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0

        # First pass: max profit if we sell on or before day i
        left_profits = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)

        # Second pass: max profit if we buy on or after day i
        right_profits = [0] * n
        max_price = prices[-1]

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profits[i] = max(right_profits[i + 1], max_price - prices[i])

        # Combine both parts
        max_total_profit = 0
        for i in range(n):
            max_total_profit = max(max_total_profit, left_profits[i] + right_profits[i])

        return max_total_profit
    

    # ✅ Example usage:
solution = Solution()
print(solution.maxProfit([3,3,5,0,0,3,1,4]))  # Output: 6
print(solution.maxProfit([1,2,3,4,5]))        # Output: 4
print(solution.maxProfit([7,6,4,3,1]))        # Output: 0