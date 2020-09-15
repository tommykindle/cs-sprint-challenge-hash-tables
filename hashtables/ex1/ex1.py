def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = dict()
    for i in range(length):
        cache[weights[i]] = i
    for i in range(length):
        items = limit - weights[i]
        if items in cache:
            return(cache[items], weights.index(weights[i]))

    return None
