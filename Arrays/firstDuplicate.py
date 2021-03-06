"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

"""

# loop through the array
# keep track of duplicates in separate array
# if duplicates is less than 1
# return that number
# if duplicates is more than 1
# find the duplicate with the smallest index
# if there are no elements (no duplicates) return -1

def firstDuplicate(a):
    # making duplicates a set
    duplicates = set()
    # for every number in duplicates
    for i in a:
        # if the number is in duplicates
        if i in duplicates:
            # return that number
            return i
        # if the number is not in duplicates, add it to the set
        else:
            duplicates.add(i)
    # if no duplicates, return -1
    return -1