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


# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

def shapeArea(n):