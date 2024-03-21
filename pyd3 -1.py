def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    # Define states for the first and second transactions
    buy1 = -prices[0]
    sell1 = 0
    buy2 = -prices[0]
    sell2 = 0

    for price in prices:
        # Update first transaction states
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)

        # Update second transaction states
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2

# Example usage:
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(max_profit(prices))  
