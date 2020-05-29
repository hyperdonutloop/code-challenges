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

# Solution 1 - 
def makeArrayConsecutive2(statues):
    #         8   -      2        + 1 = 7   - 4 = 3
    return (max(statues)-min(statues)+1) - len(statues)

# Solution 2
def makeArrayConsecutive2(statues):
    # sorting array from least to greatest
    statues.sort()
    # loops from 0 - second to last element
    firstLoop = 0
    # loops from 1 to the last element
    secondLoop = 1
    lastItem = len(statues)-1
    # diff var keeps track of the number of statues needed to fill between two consecutive numbers (see while loop)
    differences = 0
    # records number of statues that can go in-between every adjacent pair
    while (firstLoop <= lastItem - 1) and (secondLoop <= lastItem):
        # if the difference between two consecutive numbers is more than 1
        if statues[secondLoop] - statues[firstLoop] > 1:
            differences += (statues[secondLoop] - statues[firstLoop] - 1)
        # increment fl and sl as they continue the loop
        firstLoop += 1
        secondLoop += 1
    
    return differences

# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# iterate through array
# removed item and see if the array be increasing
# if it is
# return true
# if it cannot keep going to the end
# return false