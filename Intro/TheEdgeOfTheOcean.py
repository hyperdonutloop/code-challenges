# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    # initializing i 
    i = 0
    # create a variable and setting it to the product of the first pair
    maxSoFar = inputArray[i] * inputArray[i+1]
    # loop through each element, except the final one
    for i in range(len(inputArray)-1):
        # multiply each element by the one after it
        product = inputArray[i] * inputArray[i+1]
        # if it is larger, set maxSoFar to the new product
        if product > maxSoFar:
            maxSoFar = product
    # after the loop runs you will have the highest product    
    return maxSoFar