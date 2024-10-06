def max_profit(prices: list[int]) -> int:
    """
    Calculate the maximum profit from a single buy and sell of one share of stock.
    
    :param prices: List of stock prices
    :return: Maximum profit
    
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
    >>> max_profit([])
    0
    """
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    # Traverse the price list once
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5
