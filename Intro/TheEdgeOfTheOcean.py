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
    initialArea = 1
    
    return initialArea + (n * (n - 1) * 2)


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# arrange smallest to largest
# each statue will be bigger than previous by 1
# what is missing from statue array?
# [6, 2, 3, 8]
# sort 
# [2, 3, 6, 8]
# check if each one is one greater
# if it is not one greater return what the number missing

def makeArrayConsecutive2(statues):
    return (max(statues)-min(statues)+1) - len(statues)
