def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    for i in range(len(orderList)):
        totalCost = orderList[i][1]+totalCost
    return totalCost


orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] 

cost = buyLotsOfFruit(orderList)
print(cost)