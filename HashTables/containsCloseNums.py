"""
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

"""
# CLUES - 
# use  a hash table that maps each num[i] to the index i where num[i] was last seen.
# Start with an empty hash table hash. When iterating through the list num, store hash[num[i]] = i if num[i] isn't a key in the hash table. If num[i] is a key in the hash table, check if the current index and the last seen index (stored as the value) are within k of each other. 
# If not, update the last seen index in hash[num[i]] to the current index i.

nums = [0, 1, 99, 3, 5, 99]
k = 3

def containsCloseNums(nums, k):
  # creates an empty hashtable
  hashTable = {}
  # enumerate allows us to loop over something and have a counter
  # for every i/j in nums
  for i, j in enumerate(nums):
    # if j is in the hashtable AND i - hashtable at j is less than or equal to k
    if j in hashTable and i - hashTable[j] <= k:
      # return true
      return True
    # if j is not in the hashtable
    else:
      # hashtable[j] is key, value is i
      hashTable[j] = i
  # if no repeating numbers return false
  return False

containsCloseNums(nums, k)

  # create a hashtable
  # iterate through num list
  # find if nums[i] = nums[j]
  # if num[i] is not a key in the HT,
    # store hash[num[i]] = i
  
  # else if it is
    # check if current index and last seen index are within k of eachother
    # if they are not update the last seen index in hash[num[i]] to the current index i


