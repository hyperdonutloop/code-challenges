"""
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

"""
# CLUES - 
# use  a hash table that maps each num[i] to the index i where num[i] was last seen.
# Start with an empty hash table hash. When iterating through the list num, store hash[num[i]] = i if num[i] isn't a key in the hash table. If num[i] is a key in the hash table, check if the current index and the last seen index (stored as the value) are within k of each other. 
# If not, update the last seen index in hash[num[i]] to the current index i.


def containsCloseNums(nums, k):
  