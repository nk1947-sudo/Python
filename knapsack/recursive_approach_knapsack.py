def knapsack_memoized(weights: list, values: list, number_of_items: int, max_weight: int, index: int, memo: dict) -> int:
    """
    Optimized version using memoization to solve the knapsack problem.
    :param weights: A list of weights.
    :param values: A list of profits corresponding to the weights.
    :param number_of_items: Total number of items.
    :param max_weight: Maximum weight that can be carried.
    :param index: The index of the item currently being considered.
    :param memo: Dictionary for memoization to store previously computed results.
    :return: Maximum profit that can be obtained.
    """
    # Base case: No more items to process or no more capacity in the knapsack
    if index == number_of_items:
        return 0
    
    # Check if the solution to this subproblem is already computed
    if (index, max_weight) in memo:
        return memo[(index, max_weight)]
    
    # Option 1: Exclude the current item
    exclude_current_item = knapsack_memoized(weights, values, number_of_items, max_weight, index + 1, memo)
    
    # Option 2: Include the current item (if its weight allows)
    include_current_item = 0
    if weights[index] <= max_weight:
        include_current_item = values[index] + knapsack_memoized(
            weights, values, number_of_items, max_weight - weights[index], index + 1, memo
        )
    
    # Store the result in the memo table
    result = max(exclude_current_item, include_current_item)
    memo[(index, max_weight)] = result
    
    return result


def knapsack(weights: list, values: list, max_weight: int) -> int:
    """
    Wrapper function for the memoized knapsack solver.
    :param weights: A list of weights.
    :param values: A list of profits corresponding to the weights.
    :param max_weight: Maximum weight that can be carried.
    :return: Maximum profit that can be obtained.
    """
    number_of_items = len(weights)
    memo = {}
    return knapsack_memoized(weights, values, number_of_items, max_weight, 0, memo)


if __name__ == "__main__":
    weights = [1, 2, 4, 5]
    values = [5, 4, 8, 6]
    max_weight = 5
    print(knapsack(weights, values, max_weight))  # Expected output: 13

    weights2 = [3, 4, 5]
    values2 = [10, 9, 8]
    max_weight2 = 25
    print(knapsack(weights2, values2, max_weight2))  # Expected output: 27
